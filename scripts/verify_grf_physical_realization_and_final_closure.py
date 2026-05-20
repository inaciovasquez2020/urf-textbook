#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPLICIT = ROOT / "artifacts/grf/explicit_transition_shell_certificate.json"
MATCHING = ROOT / "artifacts/grf/algebraic_jet_matching_theorem.json"
PHYSICAL = ROOT / "artifacts/grf/physical_realization_theorem.json"
FINAL = ROOT / "artifacts/grf/grf_theorem_level_closure_certificate.json"
DOC = ROOT / "docs/essays/GRF_2026_PHYSICAL_REALIZATION_AND_FINAL_CLOSURE.md"

def F(x: str) -> Fraction:
    return Fraction(x)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

explicit = json.loads(EXPLICIT.read_text())
matching = json.loads(MATCHING.read_text())
physical = json.loads(PHYSICAL.read_text())
final = json.loads(FINAL.read_text())
doc = DOC.read_text()

require(physical["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED", "bad physical status")
require(physical["theorem"] == "ExplicitStressEnergyShellHasGRFPhysicalRealization", "bad physical theorem")
require(physical["remaining_import_lemmas"] == [], "physical theorem has remaining imports")

require(matching["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED", "matching theorem not closed")
require(matching["theorem"] == "AlgebraicJetMatchingImpliesGRFMatching", "matching theorem missing")

D = explicit["shell_data_D"]
real = physical["physical_realization_certificate"]
components = real["stress_energy_tensor"]["components"]

require(F(D["r1"]) == F(real["domain"]["r1"]), "r1 mismatch")
require(F(D["r2"]) == F(real["domain"]["r2"]), "r2 mismatch")
require(F(D["rho"]) == F(components["rho"]), "rho mismatch")
require(F(D["p_r"]) == F(components["p_r"]), "p_r mismatch")
require(F(D["p_t"]) == F(components["p_t"]), "p_t mismatch")

require(real["regularity"]["shell_fields_are_constant_on_certified_cells"] is True, "regularity field failure")
require(real["regularity"]["finite_cell_cover_verified"] is True, "finite cover failure")
require(real["regularity"]["boundary_C0_C1_matching_verified"] is True, "matching regularity failure")

require(real["energy_conditions"]["WEC_verified"] is True, "WEC not verified")
require(real["energy_conditions"]["DEC_verified"] is True, "DEC not verified")
require(real["energy_conditions"]["rho_minus_pt_positive_margin_verified"] is True, "positive margin not verified")

for interval in explicit["certified_intervals"]:
    require(F(interval["rho_lower_bound"]) >= 0, "WEC rho fails")
    require(F(interval["rho_plus_pr_lower_bound"]) >= 0, "WEC rho+pr fails")
    require(F(interval["rho_plus_pt_lower_bound"]) >= 0, "WEC rho+pt fails")
    require(F(interval["rho_minus_abs_pr_lower_bound"]) >= 0, "DEC rho-|pr| fails")
    require(F(interval["rho_minus_abs_pt_lower_bound"]) >= 0, "DEC rho-|pt| fails")

require(final["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED", "bad final status")
require(final["theorem"] == "GRFTheoremLevelClosureCertificate", "bad final theorem")
require(final["remaining_import_lemmas"] == [], "final closure has remaining imports")

for component in [
    "eta existence for explicit shell data D",
    "rho_minus_pt(r1) computation",
    "first-cell positivity",
    "multi-cell interval positivity",
    "WEC component inequalities",
    "DEC component inequalities",
    "AlgebraicJetMatchingImpliesGRFMatching",
    "ExplicitStressEnergyShellHasGRFPhysicalRealization",
]:
    require(component in final["closed_components"], f"missing closed component {component}")
    require(component in doc, f"doc missing closed component {component}")

for token in physical["does_not_prove"]:
    require(token in doc, f"doc missing physical boundary token {token}")

for token in final["does_not_prove"]:
    require(token in doc, f"doc missing final boundary token {token}")

print("GRF physical realization and final closure verified.")
