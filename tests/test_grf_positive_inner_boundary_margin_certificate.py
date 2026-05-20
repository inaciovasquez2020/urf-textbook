from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_positive_inner_boundary_margin_certificate_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/verify_grf_positive_inner_boundary_margin_certificate.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "verification OK" in result.stdout


def test_positive_inner_boundary_margin_artifact_is_open_interface():
    artifact = json.loads(
        (ROOT / "artifacts/grf/positive_inner_boundary_margin_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    assert artifact["status"] == "FRONTIER_OPEN_MARGIN_CERTIFICATE_INTERFACE"
    assert artifact["obligation"] == "O1_POSITIVE_INNER_BOUNDARY_MARGIN"
    assert artifact["required_object"] == "rho_minus_pt(r1) >= eta > 0"
    assert artifact["certificate_input_path"] == (
        "artifacts/grf/positive_inner_boundary_margin_input.json"
    )
    assert "GRF_2026_FULL_SOLVE_CERTIFICATE_GATE" in artifact["feeds"]
    assert any("not GRF theorem-level closure" in item for item in artifact["boundary"])


def test_positive_inner_boundary_margin_optional_input_validation_accepts_valid_data():
    script = ROOT / "scripts/verify_grf_positive_inner_boundary_margin_certificate.py"
    input_path = ROOT / "artifacts/grf/positive_inner_boundary_margin_input.json"
    try:
        input_path.write_text(
            json.dumps(
                {
                    "certificate_id": "O1_POSITIVE_INNER_BOUNDARY_MARGIN",
                    "status": "VERIFIED",
                    "rho_minus_pt_r1": 2.0,
                    "eta": 1.0,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        assert "verification OK" in result.stdout
    finally:
        input_path.unlink(missing_ok=True)
