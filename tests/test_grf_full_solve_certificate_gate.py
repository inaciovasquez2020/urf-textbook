from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_grf_full_solve_certificate_gate_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/verify_grf_full_solve_certificate_gate.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "verification OK" in result.stdout


def test_grf_full_solve_certificate_gate_has_all_eight_obligations():
    artifact = json.loads(
        (ROOT / "artifacts/grf/full_solve_certificate_gate.json").read_text(
            encoding="utf-8"
        )
    )
    obligations = {item["id"]: item for item in artifact["required_obligations"]}
    assert len(obligations) == 8
    assert "O1_POSITIVE_INNER_BOUNDARY_MARGIN" in obligations
    assert "O2_ACTUAL_DERIVATIVE_DATA" in obligations
    assert "O3_FIRST_CELL_NUMERIC_CERTIFICATE" in obligations
    assert "O4_MULTI_CELL_PROPAGATION" in obligations
    assert "O5_ALL_WEC_DEC_COMPONENTS" in obligations
    assert "O6_MATCHING_THEOREM" in obligations
    assert "O7_PHYSICAL_REALIZATION" in obligations
    assert "O8_FORMAL_VERIFICATION" in obligations
    assert all(item["status"].startswith("MISSING_") for item in obligations.values())
    assert artifact["status"] == "FRONTIER_OPEN_FULL_CERTIFICATE_GATE"
    assert any("not GRF theorem-level closure" in item for item in artifact["boundary"])
