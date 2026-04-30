from pathlib import Path

ROOT = Path("VTD_MECHANISM_PACKET")
README = ROOT / "README_BOUNDARY.md"

def test_vtd_mechanism_input_stub_exists():
    assert README.exists()
    assert (ROOT / "calibration_records").is_dir()
    assert (ROOT / "environment_logs").is_dir()
    assert (ROOT / "blinded_replication").is_dir()

def test_vtd_mechanism_input_stub_lists_required_files():
    text = README.read_text()
    assert "mechanism_off_real_001.csv" in text
    assert "mechanism_on_real_001.csv" in text
    assert "control_schedule_u_real.csv" in text
    assert "g_certificate_real.yml" in text
    assert "eps_meas_certificate_real.yml" in text
    assert "eps_F_budget_real.csv" in text
    assert "protocol_on_off_real.md" in text

def test_vtd_mechanism_input_stub_preserves_boundary():
    text = README.read_text()
    assert "input stub only" in text
    assert "contains no real empirical VTD mechanism data" in text
    assert "does not prove an anti-gravity mechanism" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "anti-gravity mechanism proven" not in text
