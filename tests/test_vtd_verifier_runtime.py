import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "vtd_verify.py"
FIXTURES = ROOT / "tests" / "fixtures" / "vtd"

def run_vtd(name: str) -> str:
    result = subprocess.run(
        [
            sys.executable,
            str(TOOL),
            str(FIXTURES / name),
            "--m", "1",
            "--g", "9.8056422",
            "--eps-meas", "0.005",
            "--eps-F", "0.001",
            "--eps-g", "0.00000005",
            "--window", "31",
            "--degree", "4",
            "--quiet",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout

def test_synthetic_ordinary_freefall_does_not_reject_h0():
    out = run_vtd("ordinary_freefall_synthetic.csv")
    assert "decision = H0_NOT_REJECTED" in out
    assert "failure to falsify ordinary force balance" in out

def test_synthetic_anomalous_freefall_rejects_h0():
    out = run_vtd("anomalous_freefall_synthetic.csv")
    assert "decision = H0_REJECTED" in out
    assert "trajectory anomaly certified under supplied measurement, force, and gravity-reference bounds" in out
    assert "physical anti-gravity mechanism not identified" in out

def test_synthetic_fixture_boundary_labels():
    readme = (FIXTURES / "README.md").read_text()
    assert "synthetic verifier fixtures" in readme
    assert "not empirical VTD data" in readme
    assert "do not identify an anti-gravity mechanism" in readme
