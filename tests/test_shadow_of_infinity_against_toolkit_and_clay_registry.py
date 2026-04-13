from pathlib import Path

def test_shadow_of_infinity_against_toolkit_and_clay_registry():
    text = Path("docs/foundations/SHADOW_OF_INFINITY.md").read_text(encoding="utf-8")
    assert r"\mathrm{ShadowOfInfinity}:=\text{a form of the finite close to infinity.}" in text

    toolkit_tools = [
        "Kairos",
        "Newstein Chain",
        "DraG0n",
        "RiGUp",
        "EV0V3",
        "EXNILIO",
        "GQu",
        "FGL",
    ]
    for item in toolkit_tools:
        assert item in text

    clay_problems = [
        "P versus NP",
        "Riemann hypothesis",
        "Navier-Stokes existence and smoothness",
        "Yang-Mills existence and mass gap",
        "Hodge conjecture",
        "Birch and Swinnerton-Dyer conjecture",
    ]
    for item in clay_problems:
        assert item in text

    assert "full Clay-problem registry" in text
    assert "compatibility check against the toolkit registry" in text
