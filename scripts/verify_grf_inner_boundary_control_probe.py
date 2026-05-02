#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_INNER_BOUNDARY_CONTROL_PROBE.md")
TOOL = Path("tools/grf_inner_boundary_control_probe.py")
ART = Path("artifacts/grf/inner_boundary_control_probe.json")

for path in (DOC, TOOL, ART):
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
for tok in [
    "Inner-Boundary Control Probe",
    "inner-boundary tangential-pressure obstruction",
    "rho-p_t",
    "quintic Hermite mass-function ansatz",
    "m''(r_1)",
    "This is an interval arithmetic frontier probe.",
    "It is not a theorem of global existence.",
    "It is not an impossibility theorem.",
    "It does not promote sampled numerical evidence to proof.",
    "It only certifies the encoded finite interval partition and ansatz family.",
    "inner-boundary tangential-pressure control with certified nonnegative rho_minus_pt and all WEC/DEC margins",
]:
    if tok not in doc:
        raise SystemExit(f"missing doc token: {tok}")

data = json.loads(ART.read_text(encoding="utf-8"))
for key in [
    "status",
    "candidate_count",
    "best_candidate",
    "targeted_cell",
    "targeted_margin",
    "next_missing_object",
    "boundary",
]:
    if key not in data:
        raise SystemExit(f"missing artifact key: {key}")

if data["status"] not in {"CERTIFIED_PASS", "FRONTIER_OPEN"}:
    raise SystemExit(f"bad status: {data['status']}")

if data["targeted_cell"] != "inner boundary cell":
    raise SystemExit("targeted_cell must be inner boundary cell")

if data["targeted_margin"] != "rho_minus_pt":
    raise SystemExit("targeted_margin must be rho_minus_pt")

best = data["best_candidate"]
for key in [
    "parameters",
    "certified_margin_lower_bounds",
    "minimum_certified_lower_bound",
    "status",
]:
    if key not in best:
        raise SystemExit(f"missing best_candidate key: {key}")

for margin in ["m_prime", "rho", "rho_minus_pr", "rho_minus_pt", "rho_plus_pr", "rho_plus_pt"]:
    if margin not in best["certified_margin_lower_bounds"]:
        raise SystemExit(f"missing margin: {margin}")

boundary = "\n".join(data["boundary"])
for tok in [
    "not a theorem of global existence",
    "not an impossibility theorem",
    "does not promote sampled numerical evidence to proof",
]:
    if tok not in boundary:
        raise SystemExit(f"missing boundary token: {tok}")

print("GRF inner-boundary control probe verification OK.")
