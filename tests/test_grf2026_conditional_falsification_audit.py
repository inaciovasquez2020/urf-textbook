import subprocess
import sys

def test_grf2026_conditional_falsification_audit_verifier():
    subprocess.run(
        [sys.executable, "tools/verify_grf2026_conditional_falsification_audit.py"],
        check=True,
    )
