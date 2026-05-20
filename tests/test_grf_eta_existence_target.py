import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/grf/eta_existence_target.json"

def test_eta_existence_target_shape():
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "FRONTIER_OPEN"
    assert data["target"] == "EtaExistence"
    assert data["minimal_missing_object"] == "analytic_eta_existence_proof"

def test_boundary_preserved():
    data = json.loads(ARTIFACT.read_text())
    assert "eta exists" in data["does_not_prove"]
    assert "rho_minus_pt(r1) has been computed" in data["does_not_prove"]
    assert "GRF theorem-level closure" in data["does_not_prove"]

def test_verifier_passes():
    subprocess.run(
        [sys.executable, "scripts/verify_grf_eta_existence_target.py"],
        cwd=ROOT,
        check=True,
    )
