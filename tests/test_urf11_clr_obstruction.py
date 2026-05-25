import subprocess
import sys
from pathlib import Path

def test_urf11_clr_obstruction_registry():
    root = Path(__file__).resolve().parents[1]
    subprocess.run(
        [sys.executable, "tools/verify_urf11_clr_obstruction.py"],
        cwd=root,
        check=True,
    )
