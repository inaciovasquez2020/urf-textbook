from pathlib import Path

def test_dreams_math_status_and_boundary():
    doc = Path("docs/dreams/DREAMS_MATH.md").read_text()
    assert "Status: CONDITIONAL_EXPOSITION_FRONTIER" in doc
    assert "It is not a theorem layer." in doc
    assert "Dreams Math is a structured idea-generation and frontier-isolation layer." in doc
    assert "unrestricted UniversalFiberEntropyGap" in doc
    assert "unrestricted Chronos-RR" in doc
    assert "unrestricted H4.1/FGL" in doc
    assert "P vs NP" in doc
    assert "any Clay problem" in doc

def test_dreams_math_is_indexed():
    idx = Path("docs/index/DOCUMENTATION_INDEX.md").read_text()
    roadmap = Path("ROADMAP.md").read_text()
    assert "docs/dreams/DREAMS_MATH.md" in idx
    assert "Dreams Math" in roadmap
