from pathlib import Path

ROOT = Path("VTD_MECHANISM_PACKET")

REQUIRED = [
    "README_BOUNDARY.md",
    "g_certificate_real.yml",
    "eps_meas_certificate_real.yml",
    "eps_F_budget_real.csv",
    "mechanism_off_real_001.csv",
    "mechanism_on_real_001.csv",
    "control_schedule_u_real.csv",
    "protocol_on_off_real.md",
]

def test_vtd_complete_input_surface_files_exist():
    for name in REQUIRED:
        assert (ROOT / name).exists(), name
    assert (ROOT / "calibration_records").is_dir()
    assert (ROOT / "environment_logs").is_dir()
    assert (ROOT / "blinded_replication").is_dir()

def test_vtd_trajectory_and_control_stubs_are_not_empirical():
    for name in [
        "mechanism_off_real_001.csv",
        "mechanism_on_real_001.csv",
        "control_schedule_u_real.csv",
    ]:
        text = (ROOT / name).read_text()
        assert "STUB_ONLY" in text
        assert "contains no real empirical VTD" in text

def test_vtd_eps_meas_stub_is_guarded():
    text = (ROOT / "eps_meas_certificate_real.yml").read_text()
    assert 'status: "STUB_ONLY"' in text
    assert "eps_meas_m_s2: null" in text
    assert "acceleration-estimator uncertainty certificate only" in text
    assert "anti-gravity mechanism proven" in text

def test_vtd_eps_f_budget_stub_is_guarded():
    text = (ROOT / "eps_F_budget_real.csv").read_text()
    assert "channel,bound_m_s2,method,evidence,status" in text
    assert "residual_drag,null,null,null,STUB_ONLY" in text
    assert "magnetic,null,null,null,STUB_ONLY" in text
    assert "recoil_or_actuator_coupling,null,null,null,STUB_ONLY" in text

def test_vtd_protocol_stub_preserves_boundary():
    text = (ROOT / "protocol_on_off_real.md").read_text()
    assert "STUB_ONLY" in text
    assert "contains no real empirical VTD mechanism protocol" in text
    assert "does not certify a trajectory anomaly" in text
    assert "does not prove an anti-gravity mechanism" in text
    assert "does not identify a physical anti-gravity mechanism" in text
    assert "not a theorem-level URF closure claim" in text
    assert "anti-gravity mechanism proven." not in text
