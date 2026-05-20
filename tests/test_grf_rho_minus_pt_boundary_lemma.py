import json
import subprocess
from pathlib import Path


def test_rho_minus_pt_boundary_lemma_artifact():
    data = json.loads(Path("artifacts/grf/rho_minus_pt_boundary_lemma.json").read_text())
    assert data["status"] == "ANALYTIC_SIGN_LEMMA"
    assert data["targeted_margin"] == "rho_minus_pt"
    assert "Phi1pp" in data["inner_boundary_inequality"]
    assert data["next_missing_object"] == "first-cell interval extension lemma for rho_minus_pt"


def test_rho_minus_pt_boundary_lemma_verifier():
    subprocess.run(["python3", "scripts/verify_grf_rho_minus_pt_boundary_lemma.py"], check=True)
