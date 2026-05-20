import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEOREM = ROOT / "artifacts/grf/algebraic_jet_matching_theorem.json"
CERT = ROOT / "artifacts/grf/explicit_transition_shell_certificate.json"

def test_matching_theorem_closed():
    data = json.loads(THEOREM.read_text())
    assert data["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED"
    assert data["theorem"] == "AlgebraicJetMatchingImpliesGRFMatching"

def test_explicit_certificate_satisfies_matching_equalities():
    cert = json.loads(CERT.read_text())
    gate = cert["matching_gate"]
    left = gate["left_boundary"]
    right = gate["right_boundary"]
    assert Fraction(left["interior_metric_value"]) == Fraction(left["shell_metric_value"])
    assert Fraction(left["interior_first_derivative"]) == Fraction(left["shell_first_derivative"])
    assert Fraction(right["shell_metric_value"]) == Fraction(right["exterior_metric_value"])
    assert Fraction(right["shell_first_derivative"]) == Fraction(right["exterior_first_derivative"])

def test_physical_realization_remains_only_import():
    data = json.loads(THEOREM.read_text())
    assert data["remaining_import_lemmas"] == ["ExplicitStressEnergyShellHasGRFPhysicalRealization"]
    assert "unconditional GRF theorem-level closure" in data["does_not_prove"]

def test_verifier_passes():
    subprocess.run(
        [sys.executable, "scripts/verify_grf_algebraic_jet_matching_theorem.py"],
        cwd=ROOT,
        check=True,
    )
