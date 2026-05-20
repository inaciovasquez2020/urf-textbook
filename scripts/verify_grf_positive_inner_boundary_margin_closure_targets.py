#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/grf/positive_inner_boundary_margin_closure_targets.json"
DOC = ROOT / "docs/essays/GRF_2026_POSITIVE_INNER_BOUNDARY_MARGIN_CLOSURE_TARGETS.md"

REQUIRED_TARGETS = [
    "EtaExistence",
    "RhoMinusPtBoundaryComputation",
    "FirstCellPositivityCertificate",
    "MultiCellIntervalCertificate",
    "WECDECClosure",
    "MatchingTheorem",
    "PhysicalRealizationTheorem",
    "GRFTheoremLevelClosure",
]

REQUIRED_BOUNDARY = [
    "eta exists",
    "rho_minus_pt(r1) has been computed",
    "first-cell positivity",
    "multi-cell interval positivity",
    "WEC/DEC closure",
    "matching theorem",
    "physical realization theorem",
    "GRF theorem-level closure",
]

data = json.loads(ARTIFACT.read_text())
doc = DOC.read_text()

assert data["status"] == "FRONTIER_OPEN"
assert [target["name"] for target in data["targets"]] == REQUIRED_TARGETS
assert data["targets"][-1]["status"] == "CONDITIONAL"
assert data["targets"][-1]["minimal_missing_object"] == "all_prior_targets_closed"

for target in data["targets"][:-1]:
    assert target["status"] == "OPEN"
    assert target["minimal_missing_object"]

for token in REQUIRED_BOUNDARY:
    assert token in data["does_not_prove"]
    assert token in doc

assert "`GRFTheoremLevelClosure` follows only after all seven predecessor targets are closed." in doc

print("GRF positive inner-boundary margin closure targets verified.")
