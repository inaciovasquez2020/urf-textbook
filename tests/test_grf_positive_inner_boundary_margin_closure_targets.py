from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/grf/positive_inner_boundary_margin_closure_targets.json"

def test_targets_exist() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert [target["name"] for target in data["targets"]] == [
        "EtaExistence",
        "RhoMinusPtBoundaryComputation",
        "FirstCellPositivityCertificate",
        "MultiCellIntervalCertificate",
        "WECDECClosure",
        "MatchingTheorem",
        "PhysicalRealizationTheorem",
        "GRFTheoremLevelClosure",
    ]

def test_all_real_targets_remain_open() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert all(target["status"] == "OPEN" for target in data["targets"][:-1])
    assert data["targets"][-1]["status"] == "CONDITIONAL"

def test_boundary_preserved() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert "GRF theorem-level closure" in data["does_not_prove"]
    assert "eta exists" in data["does_not_prove"]

def test_verifier_passes() -> None:
    subprocess.run(
        [sys.executable, "scripts/verify_grf_positive_inner_boundary_margin_closure_targets.py"],
        cwd=ROOT,
        check=True,
    )
