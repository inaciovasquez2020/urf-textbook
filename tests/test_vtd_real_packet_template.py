from pathlib import Path

DOC = Path("docs/frontier/VTD_REAL_PACKET_TEMPLATE.md")

def test_vtd_real_packet_template_exists():
    assert DOC.exists()

def test_vtd_real_packet_template_has_required_objects():
    text = DOC.read_text()
    assert "VTD_REAL_PACKET" in text
    assert "drop_real_001.csv" in text
    assert "g_certificate_real.yml" in text
    assert "eps_meas_certificate_real.yml" in text
    assert "eps_F_budget_real.csv" in text
    assert "protocol_real.md" in text
    assert "verifier_output.txt" in text

def test_vtd_real_packet_template_has_certificate_terms():
    text = DOC.read_text()
    assert r"\varepsilon_{\mathrm{meas}}" in text
    assert r"\varepsilon_F" in text
    assert r"\varepsilon_g" in text
    assert "R>0" in text

def test_vtd_real_packet_template_preserves_boundary():
    text = DOC.read_text()
    assert "contains no empirical VTD data" in text
    assert "does not certify a trajectory anomaly" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "anti-gravity mechanism proven" not in text
