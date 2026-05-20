#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_RHO_MINUS_PT_BOUNDARY_LEMMA.md")
ART = Path("artifacts/grf/rho_minus_pt_boundary_lemma.json")

for path in (DOC, ART):
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
for tok in [
    "ANALYTIC_SIGN_LEMMA",
    "\\rho-p_t",
    "beta(r)=\\frac{1}{1-2m(r)/r}",
    "\\frac{\\beta'}{\\beta}",
    "p_t",
    "\\rho-p_t",
    "\\frac{m_1'}{r_1^2}",
    "\\Phi_1''",
    "\\Phi_1'",
    "(\\rho-p_t)(r_1)\\ge0",
    "\\Phi_1'",
    "\\beta_1=\\frac{1}{1-2m_1/r_1}",
    "\\beta_1\\frac{m_1'}{r_1^2}",
    "This is an analytic sign lemma.",
    "It is not a global matching theorem.",
    "It is not a positive interval certificate.",
    "It is not WEC/DEC closure.",
    "It is not GRF theorem-level closure.",
    "first-cell interval extension lemma for rho_minus_pt",
]:
    if tok not in doc:
        raise SystemExit(f"missing doc token: {tok}")

data = json.loads(ART.read_text(encoding="utf-8"))
if data["status"] != "ANALYTIC_SIGN_LEMMA":
    raise SystemExit("bad status")
if data["targeted_margin"] != "rho_minus_pt":
    raise SystemExit("bad targeted_margin")
if data["targeted_cell"] != "inner boundary cell":
    raise SystemExit("bad targeted_cell")
if "Phi1pp" not in data["inner_boundary_inequality"]:
    raise SystemExit("missing Phi1pp in inequality")
if data["next_missing_object"] != "first-cell interval extension lemma for rho_minus_pt":
    raise SystemExit("bad next missing object")

for forbidden in [
    "global matching theorem proved",
    "positive interval certificate proved",
    "WEC/DEC closure proved",
    "GRF theorem-level closure proved",
    "physical realization theorem proved"
]:
    if forbidden in doc or forbidden in json.dumps(data):
        raise SystemExit(f"forbidden overclaim: {forbidden}")

print("GRF rho-minus-pt boundary lemma verification OK.")
