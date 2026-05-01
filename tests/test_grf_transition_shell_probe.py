import json
import subprocess
from pathlib import Path

def test_grf_transition_shell_probe_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_transition_shell_probe.py"],
        check=True,
    )

def test_grf_transition_shell_artifact_is_frontier_fail():
    payload = json.loads(Path("artifacts/grf/transition_shell_probe.json").read_text(encoding="utf-8"))
    assert payload["status"] == "FRONTIER_FAIL"
    assert any(item["value"] < 0 for item in payload["min_margins"].values())
