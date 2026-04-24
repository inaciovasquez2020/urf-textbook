from pathlib import Path

DOC = Path("docs/foundations/TRBHG.md").read_text()

def test_trbhg_status_is_expository_only():
    assert "Expository formulation only." in DOC
    assert "does not claim a new spacetime solution" in DOC

def test_trbhg_defines_time_reversal_operator():
    assert r"\mathrm{TRBHG}:=\Theta(\mathcal G_{\mathrm{BH}})" in DOC
    assert r"(\mathcal M,g,-\tau,\mathscr I^+,\mathscr I^-)" in DOC

def test_trbhg_shadow_of_infinity_identity_present():
    assert r"\operatorname{Shadow}_\tau(\mathscr I^+)" in DOC
    assert r"\operatorname{Shadow}_{-\tau}(\mathscr I^-)" in DOC
    assert r"\Theta\bigl(\operatorname{Shadow}_\tau(\mathscr I^+)\bigr)" in DOC

def test_trbhg_not_new_object_claim_locked():
    assert "TRBHG is not a new physical object." in DOC
    assert "standard white-hole/time-reversed-black-hole sector" in DOC
