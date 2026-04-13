from pathlib import Path

def test_shadow_of_infinity_scope_lock():
    text = Path("docs/foundations/SHADOW_OF_INFINITY.md").read_text(encoding="utf-8")
    assert r"\mathrm{ShadowOfInfinity}:=\text{a form of the finite close to infinity.}" in text
    assert "tested for compatibility against all toolkit tools" in text
    assert "tested against all Clay problems, solved and unsolved" in text
    assert "canonical exposition lock for Shadow of Infinity in `urf-textbook`" in text
