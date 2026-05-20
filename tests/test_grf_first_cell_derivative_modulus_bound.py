from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_first_cell_derivative_modulus_bound_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/verify_grf_first_cell_derivative_modulus_bound.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "verification OK" in result.stdout


def test_first_cell_derivative_modulus_bound_artifact_boundary():
    artifact = json.loads(
        (ROOT / "artifacts/grf/first_cell_derivative_modulus_bound.json").read_text(
            encoding="utf-8"
        )
    )
    assert artifact["status"] == "CONDITIONAL_DERIVATIVE_MODULUS_BOUND"
    assert artifact["minimal_missing_assumption_closed"] == (
        "FirstCellDerivativeData(r0,a,M0,M1,M2,P1,P2,P3)"
    )
    assert "GRF_2026_FIRST_CELL_INTERVAL_EXTENSION_LEMMA" in artifact["feeds"]
    assert any("not GRF theorem-level closure" in item for item in artifact["boundary"])
