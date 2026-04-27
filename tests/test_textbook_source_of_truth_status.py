import subprocess
import sys

def test_textbook_source_of_truth_status_guard_passes():
    subprocess.run(
        [sys.executable, "scripts/check_textbook_source_of_truth_status.py"],
        check=True,
    )
