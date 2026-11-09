"""Run with python3 -m unittest discover -s tests -p test_math_audit.py -v."""
import copy
import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('math_audit', ROOT / 'tools/math_audit.py')
ma = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ma)


def claim(lhs, rhs):
    return {'id': 'test', 'domain': 'R', 'variable': 'x', 'lhs': lhs, 'rhs': rhs}


class MathAuditTests(unittest.TestCase):
    def test_known_false(self):
        c = claim('(x + 1)**2', 'x**2 + 1')
        r = ma.audit(c)
        self.assertEqual('REFUTED', ma.verify(r, c))
        self.assertEqual({'x': 1, 'lhs': 4, 'rhs': 2}, r['certificate'][-1])

    def test_known_true(self):
        c = claim('(x + 1)**2', 'x**2 + 2*x + 1')
        r = ma.audit(c)
        self.assertEqual('EXACT_CERTIFICATE_PASS', ma.verify(r, c))
        self.assertEqual(3, len(r['certificate']))
        self.assertFalse(r['formal_kernel_verified'])

    def test_constant_and_vanishing(self):
        for a,b,expect in [('0','0','EXACT_CERTIFICATE_PASS'),
                           ('0','1','REFUTED'),('x**2-x','x*(x-1)','EXACT_CERTIFICATE_PASS'),
                           ('(x-1)*(x-2)','0','REFUTED')]:
            with self.subTest(a=a,b=b):
                c=claim(a,b);r=ma.audit(c)
                self.assertEqual(expect,ma.verify(r,c))

    def test_determinism(self):
        c=claim('2*x+x','3*x')
        self.assertEqual(ma.canonical(ma.audit(c)),ma.canonical(ma.audit(c)))

    def test_tamper_certificate(self):
        c=claim('(x+1)**2','x**2+1');r=ma.audit(c)
        r['certificate'][-1]['rhs']=4
        with self.assertRaises(ma.AuditError):ma.verify(r,c)

    def test_replay_requires_original_source(self):
        c=claim('x','x')
        with self.assertRaises(ma.AuditError):
            ma.verify(ma.audit(c))

    def test_tamper_degree(self):
        c=claim('x**3','x**3');r=ma.audit(c)
        r['degree_upper_bound']=2
        with self.assertRaises(ma.AuditError):ma.verify(r,c)

    def test_claim_substitution(self):
        c=claim('x','x');r=ma.audit(c)
        with self.assertRaises(ma.AuditError):ma.verify(r,claim('x','x+1'))

    def test_injection_rejected(self):
        for bad in ["__import__('os').system('echo bad')",'x/1','x**x', 'x**-1',
                    'x**1000','y+1','[x for x in range(1)]', '2.0*x','x < 1']:
            with self.subTest(bad=bad),self.assertRaises(ma.AuditError):
                ma.audit(claim(bad,'x'))

    def test_resource_bound(self):
        for bad in ['x**16*x**16*x','x'*513, '1000001']:
            with self.subTest(bad=bad),self.assertRaises(ma.AuditError):
                ma.audit(claim(bad,'x'))

    def test_randomized_expansions(self):
        rng=random.Random(20261107)
        for _ in range(120):
            a,b,c=(rng.randrange(-9,10) for _ in range(3))
            lhs=f'({a}*x+{b})*({a}*x+{b})+{c}'
            rhs=f'{a*a}*x**2+{2*a*b}*x+{b*b+c}'
            good=claim(lhs,rhs)
            self.assertEqual('EXACT_CERTIFICATE_PASS',ma.verify(ma.audit(good),good))
            bad=claim(lhs,f'({rhs})+1')
            self.assertEqual('REFUTED',ma.verify(ma.audit(bad),bad))

    def test_cli_roundtrip_and_overwrite_guard(self):
        with tempfile.TemporaryDirectory() as d:
            src=ROOT/'tests/fixtures/math_audit_bad_square.json'
            output=Path(d)/'report.json'
            script=str(ROOT/'tools/math_audit.py')
            a=subprocess.run([sys.executable,script,'check',str(src),'--output',str(output)],
                             text=True,capture_output=True)
            self.assertEqual(1,a.returncode,a.stderr)
            self.assertTrue(output.is_file())
            self.assertIn('STATUS := REFUTED',a.stdout)
            b=subprocess.run([sys.executable,script,'verify',str(output),'--claim',str(src)],
                             text=True,capture_output=True)
            self.assertEqual(1,b.returncode,b.stderr)
            self.assertIn('REPLAY := REFUTATION_CONFIRMED',b.stdout)
            self.assertIn('STATUS := REFUTED',b.stdout)
            self.assertNotIn('REPLAY := PASS',b.stdout)
            a2=subprocess.run([sys.executable,script,'check',str(src),'--output',str(output)],
                              text=True,capture_output=True)
            self.assertEqual(2,a2.returncode)

    def test_cli_true_identity_pass_and_malformed_error(self):
        with tempfile.TemporaryDirectory() as d:
            source = ROOT/'tests/fixtures/math_audit_true_square.json'
            report = Path(d)/'true.json'
            script = str(ROOT/'tools/math_audit.py')
            checked = subprocess.run([sys.executable,script,'check',str(source),
                                      '--output',str(report)],text=True,capture_output=True)
            self.assertEqual(0,checked.returncode,checked.stderr)
            self.assertIn('STATUS := EXACT_CERTIFICATE_PASS',checked.stdout)
            replay = subprocess.run([sys.executable,script,'verify',str(report),
                                     '--claim',str(source)],text=True,capture_output=True)
            self.assertEqual(0,replay.returncode,replay.stderr)
            self.assertIn('REPLAY := PASS',replay.stdout)
            self.assertIn('STATUS := EXACT_CERTIFICATE_PASS',replay.stdout)
            altered = json.loads(report.read_text())
            altered['certificate'][0]['rhs'] += 1
            bad = Path(d)/'tampered.json'
            bad.write_text(json.dumps(altered))
            rejected = subprocess.run([sys.executable,script,'verify',str(bad),
                                       '--claim',str(source)],text=True,capture_output=True)
            self.assertEqual(2,rejected.returncode,rejected.stderr)
            self.assertIn('AUDIT_ERROR :=',rejected.stderr)
            self.assertNotIn('REPLAY := PASS',rejected.stdout)

    def test_cli_nonascii_report_path_strict_stdout_is_error_before_write(self):
        with tempfile.TemporaryDirectory() as d:
            script = str(ROOT/'tools/math_audit.py')
            env = dict(__import__('os').environ, PYTHONIOENCODING='ascii:strict')
            for fixture in ('math_audit_bad_square.json', 'math_audit_true_square.json'):
                with self.subTest(fixture=fixture):
                    source = ROOT/'tests/fixtures'/fixture
                    report = Path(d)/('réport-' + fixture)
                    result = subprocess.run([sys.executable, script, 'check',
                                             str(source), '--output', str(report)],
                                            env=env, capture_output=True, text=True)
                    self.assertEqual(2, result.returncode, result.stderr)
                    self.assertFalse(report.exists())
                    self.assertIn('AUDIT_ERROR := report path cannot be printed',
                                  result.stderr)
                    self.assertNotIn('Traceback', result.stderr)
                    self.assertNotIn('STATUS := REFUTED', result.stdout)
            # UTF-8 stdout supports the same non-ASCII report path normally.
            source = ROOT/'tests/fixtures/math_audit_bad_square.json'
            report = Path(d)/'réport-ok.json'
            ok = subprocess.run([sys.executable, script, 'check', str(source),
                                 '--output', str(report)], capture_output=True, text=True,
                                env=dict(__import__('os').environ, PYTHONIOENCODING='utf-8'))
            self.assertEqual(1, ok.returncode, ok.stderr)
            self.assertTrue(report.exists())
            self.assertIn('STATUS := REFUTED', ok.stdout)
            self.assertIn(str(report), ok.stdout)

    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'claim.json';p.write_text('{"x":1,"x":2}')
            with self.assertRaises(ma.AuditError):ma.load_json(p)


    def test_json_read_is_bounded(self):
        from unittest import mock
        class BoundedStream:
            def __init__(self): self.size = None
            def read(self, n=-1):
                self.size = n
                if n < 0: raise AssertionError('unbounded read attempted')
                return b' '*n
            def __enter__(self): return self
            def __exit__(self, *args): return False
        stream = BoundedStream()
        with mock.patch('pathlib.Path.open', return_value=stream):
            with self.assertRaises(ma.AuditError): ma.load_json('untrusted.json')
        self.assertEqual(ma.MAX_SOURCE_BYTES * 16 + 1, stream.size)

    def test_long_integer_cli_rejected_without_traceback(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'large.json'
            p.write_text('{"n":' + '1'*5000 + '}')
            result=subprocess.run([sys.executable,str(ROOT/'tools/math_audit.py'),
                                   'check',str(p),'--output',str(Path(d)/'out.json')],
                                  capture_output=True,text=True)
            self.assertEqual(2,result.returncode,result.stderr)
            self.assertIn('AUDIT_ERROR :=',result.stderr)
            self.assertNotIn('Traceback',result.stderr)
            self.assertFalse((Path(d)/'out.json').exists())

    def test_json_oversize_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'too_large.json'
            p.write_bytes(b' '*(ma.MAX_SOURCE_BYTES*16+1))
            with self.assertRaisesRegex(ma.AuditError,'size limit'):
                ma.load_json(p)

    def test_duplicate_json_key_specific_message(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'duplicate.json'
            p.write_text('{"x":1,"x":2}')
            with self.assertRaisesRegex(ma.AuditError,'duplicate JSON key: x'):
                ma.load_json(p)


    def test_claude_surrogate_does_not_crash_cli(self):
        with tempfile.TemporaryDirectory() as d:
            c=claim('x\ud800', 'x')
            source=Path(d)/'bad.json'
            source.write_text(json.dumps(c), encoding='utf-8')
            result=subprocess.run([sys.executable,str(ROOT/'tools/math_audit.py'),
                                   'check',str(source),'--output',str(Path(d)/'r.json')],
                                  capture_output=True,text=True)
            self.assertEqual(2,result.returncode,result.stderr)
            self.assertIn('AUDIT_ERROR :=',result.stderr)
            self.assertNotIn('Traceback',result.stderr)

    def test_claude_spoofing_and_non_decimal_syntax_rejected(self):
        for lhs in ('ｘ**2','𝐱**2','1_000','0x10', 'x # comment'):
            with self.subTest(lhs=lhs),self.assertRaises(ma.AuditError):
                ma.audit(claim(lhs,'x'))

    def test_claude_intermediate_degree_guard_on_both_paths(self):
        src=claim('(x**16*x**16*x)**0','1')
        with self.assertRaises(ma.AuditError): ma.audit(src)
        valid=claim('1','1')
        forged=ma.audit(valid)
        forged['claim']=src
        forged['claim_sha256']=ma.digest(src)
        with self.assertRaises(ma.AuditError): ma.verify(forged,src)
        # The surrounding equality remains true under the ring convention.
        src2=claim('(x-x)**0','1')
        self.assertEqual('EXACT_CERTIFICATE_PASS',ma.verify(ma.audit(src2),src2))

    def test_claude_grammar_boundary_cases(self):
        for a,b in [('x**0','1'),('0**0','1'),('x**2-x*x','0'),
                    ('x**3','x**3+(x**2-x*x)*x'),('+x','x'),
                    ('(x-1)**0','1')]:
            with self.subTest(a=a):
                c=claim(a,b)
                self.assertEqual('EXACT_CERTIFICATE_PASS',ma.verify(ma.audit(c),c))
        for a in ('True*x','x**(1+1)','x**True','x\x00'):
            with self.subTest(a=a),self.assertRaises(ma.AuditError):
                ma.audit(claim(a,'x'))


if __name__ == '__main__':
    unittest.main()
