import json
import subprocess
from pathlib import Path


def test_inner_boundary_sign_condition_artifact():
    data = json.loads(Path("artifacts/grf/inner_boundary_sign_condition.json").read_text())
    assert data["status"] == "ANALYTIC_FRONTIER_CONDITION"
    assert data["targeted_margin"] == "rho_minus_pt"
    assert data["next_missing_object"] == "inner-boundary rho_minus_pt nonnegative sign lemma"


def test_inner_boundary_sign_condition_verifier():
    subprocess.run(["python3", "scripts/verify_grf_inner_boundary_sign_condition.py"], check=True)
