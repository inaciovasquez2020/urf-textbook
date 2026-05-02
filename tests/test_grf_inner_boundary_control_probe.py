import json
import subprocess
from pathlib import Path


def test_inner_boundary_control_probe_regenerates_artifact():
    subprocess.run(["python3", "tools/grf_inner_boundary_control_probe.py"], check=True)
    data = json.loads(Path("artifacts/grf/inner_boundary_control_probe.json").read_text(encoding="utf-8"))
    assert data["status"] in {"CERTIFIED_PASS", "FRONTIER_OPEN"}
    assert data["candidate_count"] > 0
    assert data["targeted_cell"] == "inner boundary cell"
    assert data["targeted_margin"] == "rho_minus_pt"
    assert "minimum_certified_lower_bound" in data["best_candidate"]


def test_inner_boundary_control_probe_verifier():
    subprocess.run(["python3", "scripts/verify_grf_inner_boundary_control_probe.py"], check=True)
