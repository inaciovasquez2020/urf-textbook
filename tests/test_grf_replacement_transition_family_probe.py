import json
import subprocess
from pathlib import Path


def test_replacement_transition_family_probe_regenerates_artifact():
    subprocess.run(["python3", "tools/grf_replacement_transition_family_probe.py"], check=True)
    data = json.loads(Path("artifacts/grf/replacement_transition_family_probe.json").read_text(encoding="utf-8"))
    assert data["status"] in {"CERTIFIED_PASS", "FRONTIER_OPEN"}
    assert data["candidate_count"] > 0
    assert data["targeted_margin"] == "rho_minus_pt"
    assert "minimum_certified_lower_bound" in data["best_candidate"]


def test_replacement_transition_family_probe_verifier():
    subprocess.run(["python3", "scripts/verify_grf_replacement_transition_family_probe.py"], check=True)
