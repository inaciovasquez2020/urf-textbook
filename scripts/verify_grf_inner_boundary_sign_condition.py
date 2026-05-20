#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_INNER_BOUNDARY_SIGN_CONDITION.md")
ART = Path("artifacts/grf/inner_boundary_sign_condition.json")

for path in (DOC, ART):
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
for tok in [
    "ANALYTIC_FRONTIER_CONDITION",
    "rho-p_t",
    "inner-boundary tangential-pressure control",
    "(\\rho-p_t)(r_1)\\ge 0",
    "\\inf_{r\\in[r_1,r_1+\\Delta r]}(\\rho-p_t)(r)\\ge0",
    "This is an analytic frontier condition.",
    "It is not a global matching theorem.",
    "It is not a positive interval certificate.",
    "It is not WEC/DEC closure.",
    "It is not GRF theorem-level closure.",
    "inner-boundary rho_minus_pt nonnegative sign lemma",
]:
    if tok not in doc:
        raise SystemExit(f"missing doc token: {tok}")

data = json.loads(ART.read_text(encoding="utf-8"))
if data["status"] != "ANALYTIC_FRONTIER_CONDITION":
    raise SystemExit("bad status")
if data["targeted_margin"] != "rho_minus_pt":
    raise SystemExit("bad targeted_margin")
if data["next_missing_object"] != "inner-boundary rho_minus_pt nonnegative sign lemma":
    raise SystemExit("bad next missing object")

for forbidden in [
    "global matching theorem proved",
    "positive interval certificate proved",
    "WEC/DEC closure proved",
    "GRF theorem-level closure proved"
]:
    if forbidden in doc or forbidden in json.dumps(data):
        raise SystemExit(f"forbidden overclaim: {forbidden}")

print("GRF inner-boundary sign condition verification OK.")
