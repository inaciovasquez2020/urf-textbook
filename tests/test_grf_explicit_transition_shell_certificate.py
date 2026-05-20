import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/grf/explicit_transition_shell_certificate.json"

def test_eta_existence_computation():
    data = json.loads(ARTIFACT.read_text())
    eta = Fraction(data["eta_certificate"]["eta"])
    rho_minus_pt_r1 = Fraction(data["eta_certificate"]["rho_minus_pt_r1"])
    assert eta > 0
    assert rho_minus_pt_r1 >= eta

def test_first_cell_and_multi_cell_bounds():
    data = json.loads(ARTIFACT.read_text())
    eta = Fraction(data["eta_certificate"]["eta"])
    for interval in data["certified_intervals"]:
        assert Fraction(interval["rho_minus_pt_lower_bound"]) >= eta

def test_wec_dec_component_inequalities():
    data = json.loads(ARTIFACT.read_text())
    for interval in data["certified_intervals"]:
        assert Fraction(interval["rho_lower_bound"]) >= 0
        assert Fraction(interval["rho_plus_pr_lower_bound"]) >= 0
        assert Fraction(interval["rho_plus_pt_lower_bound"]) >= 0
        assert Fraction(interval["rho_minus_abs_pr_lower_bound"]) >= 0
        assert Fraction(interval["rho_minus_abs_pt_lower_bound"]) >= 0

def test_matching_gate_is_algebraic_only():
    data = json.loads(ARTIFACT.read_text())
    gate = data["matching_gate"]
    assert gate["status"] == "ALGEBRAIC_JET_EQUALITY_VERIFIED"
    assert "AlgebraicJetMatchingImpliesGRFMatching" in data["conditional_import_lemmas"]
    assert "ExplicitStressEnergyShellHasGRFPhysicalRealization" in data["conditional_import_lemmas"]

def test_boundary_preserved():
    data = json.loads(ARTIFACT.read_text())
    assert "unconditional matching theorem" in data["does_not_prove"]
    assert "unconditional physical realization theorem" in data["does_not_prove"]
    assert "unconditional GRF theorem-level closure" in data["does_not_prove"]

def test_verifier_passes():
    subprocess.run(
        [sys.executable, "scripts/verify_grf_explicit_transition_shell_certificate.py"],
        cwd=ROOT,
        check=True,
    )
