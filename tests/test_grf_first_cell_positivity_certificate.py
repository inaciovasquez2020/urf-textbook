from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_first_cell_positivity_certificate_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/verify_grf_first_cell_positivity_certificate.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "verification OK" in result.stdout


def test_first_cell_positivity_certificate_artifact_boundary():
    artifact = json.loads(
        (ROOT / "artifacts/grf/first_cell_positivity_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    assert artifact["status"] == "CONDITIONAL_FIRST_CELL_CERTIFICATE"
    assert artifact["minimal_missing_assumption_closed"] == (
        "FirstCellCertificateData(eta,dr,L_cell)"
    )
    assert "GRF_2026_FIRST_CELL_INTERVAL_EXTENSION_LEMMA" in artifact["inputs"]
    assert "GRF_2026_FIRST_CELL_DERIVATIVE_MODULUS_BOUND" in artifact["inputs"]
    assert any("not GRF theorem-level closure" in item for item in artifact["boundary"])
