from pathlib import Path

DOC = Path("docs/frontier/VTD_MECHANISM_PACKET_TEMPLATE.md")

def test_vtd_mechanism_packet_template_exists():
    assert DOC.exists()

def test_vtd_mechanism_packet_template_has_required_objects():
    text = DOC.read_text()
    assert "VTD_MECHANISM_PACKET" in text
    assert "mechanism_off_real_001.csv" in text
    assert "mechanism_on_real_001.csv" in text
    assert "control_schedule_u_real.csv" in text
    assert "g_certificate_real.yml" in text
    assert "eps_meas_certificate_real.yml" in text
    assert "eps_F_budget_real.csv" in text
    assert "protocol_on_off_real.md" in text
    assert "verifier_output_off.txt" in text
    assert "verifier_output_on.txt" in text
    assert "blinded_replication" in text

def test_vtd_mechanism_packet_template_has_threshold_terms():
    text = DOC.read_text()
    assert r"\varepsilon_{\mathrm{meas}}" in text
    assert r"\varepsilon_F" in text
    assert r"\varepsilon_g" in text
    assert r"D_{\mathrm{off}}" in text
    assert r"D_{\mathrm{on}}" in text
    assert r"u(t)" in text
    assert "R(u_1)" in text
    assert "R(u_2)" in text

def test_vtd_mechanism_packet_template_preserves_boundary():
    text = DOC.read_text()
    assert "contains no empirical VTD mechanism data" in text
    assert "does not prove an anti-gravity mechanism" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "anti-gravity mechanism proven" not in text
