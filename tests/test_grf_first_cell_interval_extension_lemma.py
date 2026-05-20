import json
import subprocess
from pathlib import Path


def test_first_cell_interval_extension_lemma_artifact():
    data = json.loads(Path("artifacts/grf/first_cell_interval_extension_lemma.json").read_text())
    assert data["status"] == "CONDITIONAL_INTERVAL_EXTENSION_LEMMA"
    assert data["targeted_margin"] == "rho_minus_pt"
    assert data["targeted_cell"] == "first interval cell"
    assert data["extension_condition"] == "rho_minus_pt(r1) - L*dr >= 0"
    assert data["next_missing_object"] == "explicit derivative-modulus bound for rho_minus_pt on the first cell"


def test_first_cell_interval_extension_lemma_verifier():
    subprocess.run(["python3", "scripts/verify_grf_first_cell_interval_extension_lemma.py"], check=True)
