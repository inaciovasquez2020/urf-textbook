import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_manuscript_full_chapter_expansion_target_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_manuscript_full_chapter_expansion_target.py"],
        cwd=ROOT,
        check=True,
    )
