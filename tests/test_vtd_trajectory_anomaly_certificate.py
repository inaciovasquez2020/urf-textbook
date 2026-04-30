from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "frontier" / "VTD_TRAJECTORY_ANOMALY_CERTIFICATE.md"
TOOL = ROOT / "tools" / "vtd_verify.py"

def test_vtd_files_exist():
    assert DOC.exists()
    assert TOOL.exists()

def test_vtd_doc_boundary_is_conditional():
    text = DOC.read_text()
    assert "conditional trajectory-anomaly certificate" in text.lower()
    assert "ordinary force balance is falsified under the supplied bounds" in text
    assert "does not prove" in text
    assert "physical mechanism is anti-gravity" in text
    assert "not a theorem-level URF closure claim" in text

def test_vtd_doc_has_sharp_threshold():
    text = DOC.read_text()
    assert r"\varepsilon_{\mathrm{meas}}+\varepsilon_F+\varepsilon_g" in text
    assert "sharp rejection threshold" in text

def test_vtd_tool_preserves_claim_boundary():
    text = TOOL.read_text()
    assert "trajectory anomaly" in text
    assert "physical anti-gravity mechanism not identified" in text
    assert "H0_REJECTED" in text
    assert "H0_NOT_REJECTED" in text
    assert "eps_g" in text
