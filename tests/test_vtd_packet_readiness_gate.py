import subprocess
import sys
from pathlib import Path

TOOL = Path("tools/vtd_packet_readiness.py")

def test_vtd_packet_readiness_tool_exists():
    assert TOOL.exists()

def test_vtd_packet_readiness_rejects_stub_packet():
    proc = subprocess.run(
        [sys.executable, str(TOOL)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert proc.returncode == 1
    assert "vtd_packet_readiness = NOT_READY" in proc.stdout
    assert "STUB_ONLY" in proc.stdout
    assert "real empirical packet not yet admissible" in proc.stdout

def test_vtd_packet_readiness_preserves_boundary():
    text = TOOL.read_text()
    assert "does not certify a trajectory anomaly" in text
    assert "does not prove an anti-gravity mechanism" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "anti-gravity mechanism proven" not in text
