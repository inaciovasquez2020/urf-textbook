#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_INTERVAL_MASS_FUNCTION_TRANSITION_PROBE.md")
TOOL = Path("tools/grf_interval_mass_function_transition.py")
ART = Path("artifacts/grf/interval_mass_function_transition_probe.json")

required_doc_tokens = [
    "Interval Mass-Function Transition Probe",
    "This is an interval arithmetic frontier probe.",
    "It is not a theorem of global existence.",
    "It is not an impossibility theorem.",
    "It does not promote sampled numerical evidence to proof.",
    "It only certifies the encoded finite interval partition and ansatz family.",
    "certified positive lower bound or replacement ansatz with interval certificate",
]

required_artifact_tokens = [
    "status",
    "candidate_count",
    "best_candidate",
    "next_missing_object",
    "boundary",
]

for path in (DOC, TOOL, ART):
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
for tok in required_doc_tokens:
    if tok not in doc:
        raise SystemExit(f"missing required doc token: {tok}")

data = json.loads(ART.read_text(encoding="utf-8"))
for tok in required_artifact_tokens:
    if tok not in data:
        raise SystemExit(f"missing required artifact key: {tok}")

if data["status"] not in {"CERTIFIED_PASS", "FRONTIER_OPEN"}:
    raise SystemExit(f"bad status: {data['status']}")

if data["candidate_count"] <= 0:
    raise SystemExit("candidate_count must be positive")

best = data["best_candidate"]
if "parameters" not in best:
    raise SystemExit("missing best_candidate.parameters")

if "minimum_certified_lower_bound" not in best:
    raise SystemExit("missing best_candidate.minimum_certified_lower_bound")

if "certified_margin_lower_bounds" not in best:
    raise SystemExit("missing best_candidate.certified_margin_lower_bounds")

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

print("GRF interval mass-function transition probe verification OK.")
