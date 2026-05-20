#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/grf/eta_existence_target.json"
DOC = ROOT / "docs/essays/GRF_2026_ETA_EXISTENCE_TARGET.md"

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
assert data["target"] == "EtaExistence"
assert data["minimal_missing_object"] == "analytic_eta_existence_proof"
assert data["statement"] == "There exists eta > 0 such that rho_minus_pt(r1) >= eta."

for token in REQUIRED_BOUNDARY:
    assert token in data["does_not_prove"]
    assert token in doc

print("GRF eta existence target verified.")
