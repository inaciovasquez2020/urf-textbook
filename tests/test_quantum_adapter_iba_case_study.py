from pathlib import Path

DOC = Path("docs/case_studies/quantum_adapter_invariant_bounded_amplification_2026_05_26.md")

REQUIRED = [
    "EXTERNAL_PATTERN_EVIDENCE_ONLY",
    "invariant-bounded performance amplification",
    "small structured refinement",
    "constrained nonclassical transformation channel",
    "measurable behavior change",
    "not raw parameter scaling",
    "does not prove",
    "URF",
    "Chronos-RR",
    "H4.1/FGL",
    "P vs NP",
    "any Clay problem",
    "quantum advantage",
    "DFM-MKC",
    "not theorem evidence",
]

FORBIDDEN = [
    "proves URF",
    "proves Chronos-RR",
    "proves H4.1",
    "proves P vs NP",
    "proves quantum advantage",
    "solves any Clay problem",
    "DFM-MKC validation",
    "unrestricted theorem closure",
]


def test_quantum_adapter_case_study_boundary_tokens():
    text = DOC.read_text()
    for token in REQUIRED:
        assert token in text, token


def test_quantum_adapter_case_study_no_forbidden_promotions():
    text = DOC.read_text()
    for token in FORBIDDEN:
        assert token not in text, token
