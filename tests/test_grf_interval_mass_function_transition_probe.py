import json
import subprocess
from pathlib import Path


def test_interval_mass_function_transition_probe_regenerates_artifact():
    subprocess.run(["python3", "tools/grf_interval_mass_function_transition.py"], check=True)
    artifact = Path("artifacts/grf/interval_mass_function_transition_probe.json")
    data = json.loads(artifact.read_text(encoding="utf-8"))
    assert data["status"] in {"CERTIFIED_PASS", "FRONTIER_OPEN"}
    assert data["candidate_count"] > 0
    assert "minimum_certified_lower_bound" in data["best_candidate"]


def test_interval_mass_function_transition_probe_verifier():
    subprocess.run(["python3", "scripts/verify_grf_interval_mass_function_transition_probe.py"], check=True)
