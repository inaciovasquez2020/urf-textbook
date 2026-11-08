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
            self.assertEqual(0,a.returncode,a.stderr)
            b=subprocess.run([sys.executable,script,'verify',str(output),'--claim',str(src)],
                             text=True,capture_output=True)
            self.assertEqual(0,b.returncode,b.stderr)
            self.assertIn('REPLAY := PASS',b.stdout)
            a2=subprocess.run([sys.executable,script,'check',str(src),'--output',str(output)],
                              text=True,capture_output=True)
            self.assertEqual(2,a2.returncode)

    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'claim.json';p.write_text('{"x":1,"x":2}')
            with self.assertRaises(ma.AuditError):ma.load_json(p)


if __name__ == '__main__':
    unittest.main()
