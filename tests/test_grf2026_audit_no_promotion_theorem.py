import subprocess
import sys


def test_grf2026_audit_no_promotion_theorem_verifier():
    subprocess.run(
        [sys.executable, "tools/verify_grf2026_audit_no_promotion_theorem.py"],
        check=True,
    )
