import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_manuscript_chapter_completeness_audit_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_manuscript_chapter_completeness_audit.py"],
        cwd=ROOT,
        check=True,
    )
