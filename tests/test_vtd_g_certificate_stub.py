from pathlib import Path

CERT = Path("VTD_MECHANISM_PACKET/g_certificate_real.yml")

def test_vtd_g_certificate_stub_exists():
    assert CERT.exists()

def test_vtd_g_certificate_stub_has_required_fields():
    text = CERT.read_text()
    assert 'source_class: "IBGE BDG / Rede Gravimetrica"' in text
    assert 'station_type: "Estacao Gravimetrica - EG"' in text
    assert "station_or_site: null" in text
    assert "gravity_mgal: null" in text
    assert "g_cert_m_s2: null" in text
    assert "eps_g_m_s2: null" in text
    assert "g_cert_m_s2 = gravity_mgal * 1.0e-5" in text

def test_vtd_g_certificate_stub_preserves_boundary():
    text = CERT.read_text()
    assert "gravity-reference certificate only" in text
    assert "trajectory anomaly certified" in text
    assert "anti-gravity mechanism proven" in text
    assert "physical anti-gravity mechanism identified" in text
    assert "theorem-level URF closure" in text
