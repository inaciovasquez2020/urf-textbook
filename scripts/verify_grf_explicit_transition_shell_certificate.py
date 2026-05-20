#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/grf/explicit_transition_shell_certificate.json"
DOC = ROOT / "docs/essays/GRF_2026_EXPLICIT_TRANSITION_SHELL_CERTIFICATE.md"

def F(value: str) -> Fraction:
    return Fraction(value)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

data = json.loads(ARTIFACT.read_text())
doc = DOC.read_text()

require(data["status"] == "CONDITIONAL_EXPLICIT_CERTIFICATE_PHYSICAL_REALIZATION_IMPORT_OPEN", "bad status")

D = data["shell_data_D"]
rho = F(D["rho"])
pr = F(D["p_r"])
pt = F(D["p_t"])
rho_minus_pt = F(D["rho_minus_pt"])

require(F(D["r1"]) < F(D["r2"]), "bad shell radii")
require(rho_minus_pt == rho - pt, "rho_minus_pt mismatch")

eta = F(data["eta_certificate"]["eta"])
rho_minus_pt_r1 = F(data["eta_certificate"]["rho_minus_pt_r1"])

require(eta > 0, "eta is not positive")
require(rho_minus_pt_r1 == rho_minus_pt, "rho_minus_pt(r1) mismatch")
require(rho_minus_pt_r1 >= eta, "eta lower bound fails")

previous_b = None
for interval in data["certified_intervals"]:
    a = F(interval["a"])
    b = F(interval["b"])
    require(a < b, f"bad interval {interval['name']}")
    if previous_b is not None:
        require(a == previous_b, f"interval cover gap at {interval['name']}")
    previous_b = b

    require(F(interval["rho_minus_pt_lower_bound"]) == rho - pt, f"rho_minus_pt lower bound mismatch on {interval['name']}")
    require(F(interval["rho_lower_bound"]) == rho, f"rho lower bound mismatch on {interval['name']}")
    require(F(interval["rho_plus_pr_lower_bound"]) == rho + pr, f"WEC rho+pr mismatch on {interval['name']}")
    require(F(interval["rho_plus_pt_lower_bound"]) == rho + pt, f"WEC rho+pt mismatch on {interval['name']}")
    require(F(interval["rho_minus_abs_pr_lower_bound"]) == rho - abs(pr), f"DEC rho-|pr| mismatch on {interval['name']}")
    require(F(interval["rho_minus_abs_pt_lower_bound"]) == rho - abs(pt), f"DEC rho-|pt| mismatch on {interval['name']}")

    require(F(interval["rho_minus_pt_lower_bound"]) >= eta, f"first/multi-cell eta bound fails on {interval['name']}")
    require(F(interval["rho_lower_bound"]) >= 0, f"WEC rho fails on {interval['name']}")
    require(F(interval["rho_plus_pr_lower_bound"]) >= 0, f"WEC rho+pr fails on {interval['name']}")
    require(F(interval["rho_plus_pt_lower_bound"]) >= 0, f"WEC rho+pt fails on {interval['name']}")
    require(F(interval["rho_minus_abs_pr_lower_bound"]) >= 0, f"DEC rho-|pr| fails on {interval['name']}")
    require(F(interval["rho_minus_abs_pt_lower_bound"]) >= 0, f"DEC rho-|pt| fails on {interval['name']}")

require(previous_b == F(D["r2"]), "interval cover does not end at r2")

gate = data["matching_gate"]
require(gate["status"] == "ALGEBRAIC_JET_EQUALITY_VERIFIED", "bad matching gate status")

left = gate["left_boundary"]
right = gate["right_boundary"]
require(F(left["interior_metric_value"]) == F(left["shell_metric_value"]), "left C0 matching fails")
require(F(left["interior_first_derivative"]) == F(left["shell_first_derivative"]), "left C1 matching fails")
require(F(right["shell_metric_value"]) == F(right["exterior_metric_value"]), "right C0 matching fails")
require(F(right["shell_first_derivative"]) == F(right["exterior_first_derivative"]), "right C1 matching fails")

for lemma in [
    "AlgebraicJetMatchingImpliesGRFMatching",
    "ExplicitStressEnergyShellHasGRFPhysicalRealization",
]:
    require(lemma in data["conditional_import_lemmas"], f"missing conditional lemma {lemma}")
    require(lemma in doc, f"doc missing conditional lemma {lemma}")

for token in data["does_not_prove"]:
    require(token in doc, f"doc missing boundary token {token}")

print("GRF explicit transition-shell certificate verified.")
