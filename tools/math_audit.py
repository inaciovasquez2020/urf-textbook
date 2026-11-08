#!/usr/bin/env python3
"""Experimental exact audit for univariate integer-polynomial equalities.

Security boundary: an AST whitelist is used; input expressions are never eval'd.
Proof boundary: certificates are finite exact arithmetic plus a stated degree bound,
not Lean kernel proofs and not arbitrary mathematical argument verification.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import sys
from pathlib import Path

SCHEMA = 'urf-textbook.math-audit.v0.1'
MAX_SOURCE_BYTES = 4096
MAX_EXPR_CHARS = 512
MAX_AST_NODES = 120
MAX_EXPONENT = 16
MAX_DEGREE = 32
MAX_BITS = 8192


class AuditError(ValueError):
    pass


def _no_duplicates(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise AuditError('duplicate JSON key: ' + key)
        obj[key] = value
    return obj


def _reject_constant(token):
    raise AuditError('nonstandard JSON constant: ' + token)


def load_json(path):
    # Read at most one byte beyond the limit to avoid unbounded memory use.
    with Path(path).open('rb') as stream:
        blob = stream.read(MAX_SOURCE_BYTES * 16 + 1)
    if len(blob) > MAX_SOURCE_BYTES * 16:
        raise AuditError('JSON file exceeds size limit')
    try:
        obj = json.loads(blob.decode('utf-8'), object_pairs_hook=_no_duplicates,
                         parse_constant=_reject_constant)
    except AuditError:
        raise
    except (UnicodeError, json.JSONDecodeError, ValueError, RecursionError) as exc:
        raise AuditError('invalid UTF-8 JSON') from exc
    return obj


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('ascii')


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def guard_int(value):
    if type(value) is not int or value.bit_length() > MAX_BITS:
        raise AuditError('integer/operation exceeds resource limit')
    return value


def parse_expr(src):
    if type(src) is not str or len(src) > MAX_EXPR_CHARS or not src:
        raise AuditError('expression must be a nonempty short string')
    # Restrict source spelling, not merely the NFKC-normalized Python AST.
    # This also excludes Python comments, hexadecimal and underscored literals.
    if any(ch not in '0123456789x+-*() \t\r\n' for ch in src):
        raise AuditError('expression contains characters outside the ASCII polynomial grammar')
    if '0x' in src:
        raise AuditError('hexadecimal literals are not supported')
    try:
        tree = ast.parse(src, mode='eval')
    except (SyntaxError, RecursionError, ValueError) as exc:
        raise AuditError('invalid expression syntax') from exc
    nodes = list(ast.walk(tree))
    if len(nodes) > MAX_AST_NODES:
        raise AuditError('expression AST exceeds node limit')

    def degree(n):
        def bounded(d):
            if d > MAX_DEGREE:
                raise AuditError('intermediate degree bound exceeds 32')
            return d
        if isinstance(n, ast.Expression):
            return degree(n.body)
        if isinstance(n, ast.Constant) and type(n.value) is int:
            if abs(n.value) > 1_000_000:
                raise AuditError('integer literal out of range')
            return 0
        if isinstance(n, ast.Name) and n.id == 'x':
            return 1
        if isinstance(n, ast.UnaryOp) and type(n.op) in (ast.UAdd, ast.USub):
            return degree(n.operand)
        if isinstance(n, ast.BinOp):
            if type(n.op) in (ast.Add, ast.Sub):
                return bounded(max(degree(n.left), degree(n.right)))
            if type(n.op) is ast.Mult:
                return bounded(degree(n.left) + degree(n.right))
            if type(n.op) is ast.Pow:
                if not (isinstance(n.right, ast.Constant) and type(n.right.value) is int
                        and 0 <= n.right.value <= MAX_EXPONENT):
                    raise AuditError('exponent must be a literal integer 0..16')
                return bounded(degree(n.left) * n.right.value)
        raise AuditError('unsupported expression: only integers, x, +, -, *, **')

    try:
        bound = degree(tree)
    except RecursionError as exc:
        raise AuditError('expression too deeply nested') from exc
    if bound > MAX_DEGREE:
        raise AuditError('degree bound exceeds 32')
    return tree.body, bound


def poly(node):
    """Coefficient-normalization implementation (separate from direct evaluator)."""
    def trim(p):
        while len(p) > 1 and p[-1] == 0:
            p.pop()
        if len(p) > MAX_DEGREE + 1:
            raise AuditError('polynomial degree limit exceeded')
        return tuple(guard_int(c) for c in p)

    def add(a, b, sign=1):
        return trim([guard_int((a[i] if i < len(a) else 0) +
                               sign * (b[i] if i < len(b) else 0))
                     for i in range(max(len(a), len(b)))])

    def mul(a, b):
        out = [0] * (len(a) + len(b) - 1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                out[i + j] = guard_int(out[i + j] + ai * bj)
        return trim(out)

    def rec(n):
        if isinstance(n, ast.Constant):
            return (n.value,)
        if isinstance(n, ast.Name):
            return (0, 1)
        if isinstance(n, ast.UnaryOp):
            a = rec(n.operand)
            return a if isinstance(n.op, ast.UAdd) else tuple(-v for v in a)
        if isinstance(n.op, ast.Add):
            return add(rec(n.left), rec(n.right))
        if isinstance(n.op, ast.Sub):
            return add(rec(n.left), rec(n.right), -1)
        if isinstance(n.op, ast.Mult):
            return mul(rec(n.left), rec(n.right))
        if isinstance(n.op, ast.Pow):
            base, exponent = rec(n.left), n.right.value
            out = (1,)
            for _ in range(exponent):
                out = mul(out, base)
            return out
        raise AuditError('invalid AST node')
    return rec(node)


def direct_eval(node, x):
    """Independent AST integer evaluation, not using polynomial coefficients."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return x
    if isinstance(node, ast.UnaryOp):
        a = direct_eval(node.operand, x)
        return guard_int(a if isinstance(node.op, ast.UAdd) else -a)
    a = direct_eval(node.left, x)
    if isinstance(node.op, ast.Pow):
        return guard_int(pow(a, node.right.value))
    b = direct_eval(node.right, x)
    if isinstance(node.op, ast.Add):
        return guard_int(a + b)
    if isinstance(node.op, ast.Sub):
        return guard_int(a - b)
    if isinstance(node.op, ast.Mult):
        return guard_int(a * b)
    raise AuditError('invalid AST node')


def parse_claim(obj):
    if type(obj) is not dict or set(obj) != {'id', 'domain', 'variable', 'lhs', 'rhs'}:
        raise AuditError('claim must have exactly id, domain, variable, lhs, rhs')
    if type(obj['id']) is not str or not (1 <= len(obj['id']) <= 100):
        raise AuditError('invalid claim id')
    if obj['domain'] != 'R' or obj['variable'] != 'x':
        raise AuditError('only domain R and variable x are supported')
    left, dl = parse_expr(obj['lhs'])
    right, dr = parse_expr(obj['rhs'])
    return left, right, max(dl, dr)


def audit(obj):
    lhs, rhs, degree = parse_claim(obj)
    lp, rp = poly(lhs), poly(rhs)
    certificate = []
    for x in range(degree + 1):
        lv, rv = direct_eval(lhs, x), direct_eval(rhs, x)
        certificate.append({'x': x, 'lhs': lv, 'rhs': rv})
        if lv != rv:
            break
    status = 'REFUTED' if certificate[-1]['lhs'] != certificate[-1]['rhs'] else 'EXACT_CERTIFICATE_PASS'
    if (lp == rp) != (status == 'EXACT_CERTIFICATE_PASS'):
        raise AuditError('internal polynomial/evaluation disagreement')
    if status == 'EXACT_CERTIFICATE_PASS' and len(certificate) != degree + 1:
        raise AuditError('missing exact evaluations')
    return {
        'schema': SCHEMA,
        'scope': 'univariate integer-coefficient polynomial identity over R',
        'claim': obj,
        'claim_sha256': digest(obj),
        'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status': status,
        'degree_upper_bound': degree,
        'certificate': certificate,
        'method': ('distinct integer evaluations at x=0..d, with syntactic degree upper bound d; '
                   'nonzero polynomial of degree <=d cannot have d+1 distinct roots'),
        'formal_kernel_verified': False,
    }


def verify(report, claim=None):
    if claim is None:
        raise AuditError('original source claim required for replay')
    if type(report) is not dict or set(report) != {
        'schema', 'scope', 'claim', 'claim_sha256', 'implementation_sha256',
        'status', 'degree_upper_bound', 'certificate', 'method', 'formal_kernel_verified'
    }:
        raise AuditError('invalid report shape')
    if report['schema'] != SCHEMA:
        raise AuditError('unknown report schema')
    if report['scope'] != 'univariate integer-coefficient polynomial identity over R':
        raise AuditError('incorrect claimed scope')
    if report['formal_kernel_verified'] is not False:
        raise AuditError('false formal-kernel status')
    if report['claim_sha256'] != digest(report['claim']):
        raise AuditError('embedded claim digest mismatch')
    if report['implementation_sha256'] != hashlib.sha256(Path(__file__).read_bytes()).hexdigest():
        raise AuditError('checker source digest mismatch')
    if canonical(claim) != canonical(report['claim']):
        raise AuditError('report claim does not match supplied source claim')
    left, right, d = parse_claim(report['claim'])
    if type(report['degree_upper_bound']) is not int or report['degree_upper_bound'] != d:
        raise AuditError('incorrect degree bound')
    if report['method'] != ('distinct integer evaluations at x=0..d, with syntactic degree upper bound d; '
                            'nonzero polynomial of degree <=d cannot have d+1 distinct roots'):
        raise AuditError('invalid proof method')
    cert = report['certificate']
    if type(cert) is not list or not (1 <= len(cert) <= d + 1):
        raise AuditError('invalid certificate length')
    for i, item in enumerate(cert):
        if (type(item) is not dict or set(item) != {'x', 'lhs', 'rhs'} or
                any(type(item[k]) is not int for k in item)):
            raise AuditError('invalid certificate entry')
        if item != {'x': i, 'lhs': direct_eval(left, i), 'rhs': direct_eval(right, i)}:
            raise AuditError('certificate arithmetic mismatch')
    bad_positions = [i for i, item in enumerate(cert) if item['lhs'] != item['rhs']]
    if report['status'] == 'REFUTED':
        if bad_positions != [len(cert) - 1]:
            raise AuditError('refutation lacks a first witness')
    elif report['status'] == 'EXACT_CERTIFICATE_PASS':
        if bad_positions or len(cert) != d + 1:
            raise AuditError('identity lacks d+1 exact equal evaluations')
    else:
        raise AuditError('unrecognized status')
    return report['status']


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='cmd', required=True)
    check = sub.add_parser('check', help='audit JSON claim and write exact certificate')
    check.add_argument('claim')
    check.add_argument('--output', required=True)
    replay = sub.add_parser('verify', help='replay report using a separate evaluation algorithm')
    replay.add_argument('report')
    replay.add_argument('--claim', required=True, help='original JSON claim for input binding')
    args = parser.parse_args(argv)
    try:
        if args.cmd == 'check':
            out = Path(args.output)
            if out.exists():
                raise AuditError('output exists; refusing overwrite')
            report = audit(load_json(args.claim))
            verify(report, load_json(args.claim))
            with out.open('xb') as handle:
                handle.write(json.dumps(report, indent=2, sort_keys=True).encode() + b'\n')
            print('STATUS := ' + report['status'])
            print('CLAIM_SHA256 := ' + report['claim_sha256'])
            print('REPORT := ' + str(out))
        else:
            report = load_json(args.report)
            status = verify(report, load_json(args.claim))
            print('REPLAY := PASS')
            print('STATUS := ' + status)
    except (AuditError, OSError, RecursionError, OverflowError) as exc:
        print('AUDIT_ERROR := ' + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
