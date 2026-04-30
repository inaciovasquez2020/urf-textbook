import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "vtd"
TOOL = ROOT / "tools" / "vtd_mechanism_verify.py"


def run_mechanism(off: str, on: str):
    return subprocess.run(
        [
            sys.executable,
            str(TOOL),
            "--off", str(FIXTURES / off),
            "--on", str(FIXTURES / on),
            "--control", str(FIXTURES / "control_schedule_synthetic.csv"),
            "--m", "1.0",
            "--g", "9.8056422",
            "--eps-meas", "0.005",
            "--eps-F", "0.001",
            "--eps-g", "0.00000005",
            "--window", "31",
            "--degree", "4",
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def test_vtd_mechanism_verifier_certifies_on_off_pattern():
    proc = run_mechanism("ordinary_freefall_synthetic.csv", "anomalous_freefall_synthetic.csv")
    assert proc.returncode == 0
    assert "off_decision = H0_NOT_REJECTED" in proc.stdout
    assert "on_decision = H0_REJECTED" in proc.stdout
    assert "mechanism_packet_decision = ON_OFF_ANOMALY_PATTERN_CERTIFIED" in proc.stdout
    assert "physical anti-gravity mechanism not identified" in proc.stdout


def test_vtd_mechanism_verifier_rejects_nonpattern():
    proc = run_mechanism("ordinary_freefall_synthetic.csv", "ordinary_freefall_synthetic.csv")
    assert proc.returncode == 1
    assert "mechanism_packet_decision = ON_OFF_ANOMALY_PATTERN_NOT_CERTIFIED" in proc.stdout
    assert "physical anti-gravity mechanism not identified" in proc.stdout


def test_vtd_mechanism_verifier_preserves_boundary():
    text = TOOL.read_text()
    assert "does not prove an anti-gravity mechanism" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "anti-gravity mechanism proven" not in text
