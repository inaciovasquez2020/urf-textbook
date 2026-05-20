#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEOREM = ROOT / "artifacts/grf/algebraic_jet_matching_theorem.json"
CERT = ROOT / "artifacts/grf/explicit_transition_shell_certificate.json"
DOC = ROOT / "docs/essays/GRF_2026_ALGEBRAIC_JET_MATCHING_THEOREM.md"

def F(x: str) -> Fraction:
    return Fraction(x)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

theorem = json.loads(THEOREM.read_text())
cert = json.loads(CERT.read_text())
doc = DOC.read_text()

require(theorem["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED", "bad theorem status")
require(theorem["theorem"] == "AlgebraicJetMatchingImpliesGRFMatching", "bad theorem name")

definition = theorem["predicate_definition"]["GRFMatchingCertificate"]
for field in [
    "left_boundary_C0_equality",
    "left_boundary_C1_equality",
    "right_boundary_C0_equality",
    "right_boundary_C1_equality",
]:
    require(field in definition, f"missing matching field {field}")

gate = cert["matching_gate"]
require(gate["status"] == "ALGEBRAIC_JET_EQUALITY_VERIFIED", "source gate not verified")

left = gate["left_boundary"]
right = gate["right_boundary"]

require(F(left["interior_metric_value"]) == F(left["shell_metric_value"]), "left C0 equality fails")
require(F(left["interior_first_derivative"]) == F(left["shell_first_derivative"]), "left C1 equality fails")
require(F(right["shell_metric_value"]) == F(right["exterior_metric_value"]), "right C0 equality fails")
require(F(right["shell_first_derivative"]) == F(right["exterior_first_derivative"]), "right C1 equality fails")

require(
    theorem["remaining_import_lemmas"] == ["ExplicitStressEnergyShellHasGRFPhysicalRealization"],
    "unexpected remaining import lemmas",
)

for token in theorem["does_not_prove"]:
    require(token in doc, f"doc missing boundary token {token}")

require("AlgebraicJetMatchingImpliesGRFMatching" in doc, "doc missing theorem name")
require("UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED" in doc, "doc missing status")

print("GRF algebraic jet matching theorem verified.")
