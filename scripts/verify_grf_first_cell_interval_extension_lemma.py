#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_FIRST_CELL_INTERVAL_EXTENSION_LEMMA.md")
ART = Path("artifacts/grf/first_cell_interval_extension_lemma.json")

for path in (DOC, ART):
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
for tok in [
    "CONDITIONAL_INTERVAL_EXTENSION_LEMMA",
    "\\rho-p_t",
    "I_1=[r_1,r_1+\\Delta r]",
    "f(r)=\\rho(r)-p_t(r)",
    "f(r_1)\\ge \\eta",
    "|f'(r)|\\le L",
    "\\eta-L\\Delta r\\ge0",
    "\\inf_{r\\in[r_1,r_1+\\Delta r]} f(r)\\ge0",
    "mean-value inequality",
    "explicit derivative-modulus bound for rho_minus_pt on the first cell",
    "This is a conditional interval extension lemma.",
    "It is not an existence proof for the derivative-modulus bound.",
    "It is not a positive interval certificate.",
    "It is not a global matching theorem.",
    "It is not WEC/DEC closure.",
    "It is not GRF theorem-level closure."
]:
    if tok not in doc:
        raise SystemExit(f"missing doc token: {tok}")

data = json.loads(ART.read_text(encoding="utf-8"))
if data["status"] != "CONDITIONAL_INTERVAL_EXTENSION_LEMMA":
    raise SystemExit("bad status")
if data["targeted_margin"] != "rho_minus_pt":
    raise SystemExit("bad targeted_margin")
if data["targeted_cell"] != "first interval cell":
    raise SystemExit("bad targeted_cell")
if data["extension_condition"] != "rho_minus_pt(r1) - L*dr >= 0":
    raise SystemExit("bad extension condition")
if data["next_missing_object"] != "explicit derivative-modulus bound for rho_minus_pt on the first cell":
    raise SystemExit("bad next missing object")

for forbidden in [
    "positive interval certificate proved",
    "global matching theorem proved",
    "WEC/DEC closure proved",
    "GRF theorem-level closure proved",
    "physical realization theorem proved"
]:
    if forbidden in doc or forbidden in json.dumps(data):
        raise SystemExit(f"forbidden overclaim: {forbidden}")

print("GRF first-cell interval extension lemma verification OK.")
