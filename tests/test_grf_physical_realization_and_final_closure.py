import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHYSICAL = ROOT / "artifacts/grf/physical_realization_theorem.json"
FINAL = ROOT / "artifacts/grf/grf_theorem_level_closure_certificate.json"

def test_physical_realization_closed():
    data = json.loads(PHYSICAL.read_text())
    assert data["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED"
    assert data["theorem"] == "ExplicitStressEnergyShellHasGRFPhysicalRealization"
    assert data["remaining_import_lemmas"] == []

def test_final_closure_closed():
    data = json.loads(FINAL.read_text())
    assert data["status"] == "UNCONDITIONAL_CERTIFICATE_THEOREM_CLOSED"
    assert data["theorem"] == "GRFTheoremLevelClosureCertificate"
    assert data["remaining_import_lemmas"] == []

def test_final_closure_components_present():
    data = json.loads(FINAL.read_text())
    required = {
        "eta existence for explicit shell data D",
        "rho_minus_pt(r1) computation",
        "first-cell positivity",
        "multi-cell interval positivity",
        "WEC component inequalities",
        "DEC component inequalities",
        "AlgebraicJetMatchingImpliesGRFMatching",
        "ExplicitStressEnergyShellHasGRFPhysicalRealization",
    }
    assert required.issubset(set(data["closed_components"]))

def test_boundary_preserved():
    data = json.loads(FINAL.read_text())
    assert "global uniqueness of the realized spacetime" in data["does_not_prove"]
    assert "maximal analytic extension" in data["does_not_prove"]
    assert "nonlinear stability under arbitrary perturbations" in data["does_not_prove"]
    assert "observational realization in the physical universe" in data["does_not_prove"]
    assert "any Clay problem" in data["does_not_prove"]

def test_verifier_passes():
    subprocess.run(
        [sys.executable, "scripts/verify_grf_physical_realization_and_final_closure.py"],
        cwd=ROOT,
        check=True,
    )
