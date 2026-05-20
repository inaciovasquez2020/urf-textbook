import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_grf_theorem_level_closure_overclaim_audit_passes():
    subprocess.run(
        ["python3", "scripts/audit_grf_theorem_level_closure_overclaims.py"],
        cwd=ROOT,
        check=True,
    )
