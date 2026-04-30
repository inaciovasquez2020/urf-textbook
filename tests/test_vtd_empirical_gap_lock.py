from pathlib import Path

DOC = Path("docs/status/VTD_EMPIRICAL_GAP_LOCK_2026_04_30.md")

def test_vtd_empirical_gap_lock_exists():
    assert DOC.exists()

def test_vtd_empirical_gap_lock_lists_completed_layers():
    text = DOC.read_text()
    assert "VTD trajectory-anomaly certificate" in text
    assert "VTD trajectory verifier" in text
    assert "ON/OFF mechanism-pattern verifier" in text
    assert "real-packet readiness gate" in text

def test_vtd_empirical_gap_lock_names_unique_remaining_object():
    text = DOC.read_text()
    assert "unique remaining object is a real empirical ON/OFF VTD mechanism packet" in text
    assert "mechanism_off_real_001.csv" in text
    assert "mechanism_on_real_001.csv" in text
    assert "control_schedule_u_real.csv" in text
    assert "g_certificate_real.yml" in text
    assert "eps_meas_certificate_real.yml" in text
    assert "eps_F_budget_real.csv" in text
    assert "protocol_on_off_real.md" in text
    assert "blinded_replication" in text

def test_vtd_empirical_gap_lock_preserves_boundary():
    text = DOC.read_text()
    assert "does not certify a trajectory anomaly" in text
    assert "does not prove an anti-gravity mechanism" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "No further progress possible without replacing the stubs" in text
    assert "anti-gravity mechanism proven" not in text
