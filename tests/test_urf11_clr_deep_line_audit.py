import subprocess
import sys
from pathlib import Path

def test_urf11_clr_deep_line_audit():
    root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [sys.executable, "tools/verify_urf11_clr_deep_line_audit.py"],
        cwd=root,
        check=True,
    )
