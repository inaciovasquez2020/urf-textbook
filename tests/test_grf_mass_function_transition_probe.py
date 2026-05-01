import json
import subprocess
from pathlib import Path

def test_grf_mass_function_transition_probe_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_mass_function_transition_probe.py"],
        check=True,
    )

def test_grf_mass_function_transition_probe_artifact_boundary():
    payload = json.loads(Path("artifacts/grf/mass_function_transition_probe.json").read_text(encoding="utf-8"))
    assert payload["status"] in {"PASS_NUMERICAL_SAMPLE", "FRONTIER_FAIL"}
    assert payload["next_missing_object"] == "interval-certified mass-function transition ansatz"
    assert payload["candidate_count"] > 0
