from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_19.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_19_review.md"

REQUIRED_PAGE = [
    "Example: Riemann Hypothesis",
    "Euler–Gram operator",
    "rigidity principles",
    "Spectral coercivity prevents drift",
    "capacity-escaping mode",
]

REQUIRED_REVIEW = [
    "v0.1.2 Page 19 Review",
    "Status: `BOUNDARY_CLARIFICATION`",
    "Extract: `docs/page_audits/v0.1.2/page_19.txt`",
    "Riemann Hypothesis example sentence",
    "interpretive framework language only",
    "textbook-level analogy",
    "Euler-Gram spectral coercivity",
    "capacity-escape obstruction language",
    "does not prove",
    "the Riemann Hypothesis",
    "Euler-Gram coercivity",
    "positivity of the Euler-Gram operator",
    "any Clay problem",
    "unrestricted Chronos-RR",
    "H4.1/FGL",
    "P vs NP",
    "theorem-level closure of the capacity-escape principle",
    "No source rewrite is required",
    "`BOUNDARY_CLARIFICATION`",
]

FORBIDDEN_REVIEW = [
    "proves the Riemann Hypothesis",
    "solves the Riemann Hypothesis",
    "proves Euler-Gram coercivity",
    "proves positivity of the Euler-Gram operator",
    "solves any Clay problem",
    "proves Chronos-RR",
    "proves H4.1/FGL",
    "proves P vs NP",
    "theorem closure achieved",
]


def test_page_19_extract_tokens():
    text = PAGE.read_text()
    for token in REQUIRED_PAGE:
        assert token in text, token


def test_page_19_review_tokens():
    text = REVIEW.read_text()
    for token in REQUIRED_REVIEW:
        assert token in text, token


def test_page_19_review_no_forbidden_promotions():
    text = REVIEW.read_text()
    for token in FORBIDDEN_REVIEW:
        assert token not in text, token


def test_page_19_plan_updated():
    text = PLAN.read_text()
    assert "| 19 | `docs/page_audits/v0.1.2/page_19.txt` | BOUNDARY_CLARIFICATION |" in text
    assert "docs/page_audits/v0.1.2/reviews/page_19_review.md" in text
