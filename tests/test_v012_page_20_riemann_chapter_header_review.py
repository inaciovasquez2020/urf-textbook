from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_20.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_20_review.md"

REQUIRED_PAGE = [
    "CHAPTER 7",
    "RIEMANN HYPOTHESIS",
]

REQUIRED_REVIEW = [
    "v0.1.2 Page 20 Review",
    "Status: `NO_CHANGE`",
    "Extract: `docs/page_audits/v0.1.2/page_20.txt`",
    "chapter-header continuation page",
    "Riemann Hypothesis",
    "does not introduce a new theorem-closure claim",
    "Riemann Hypothesis proof claim",
    "Euler-Gram coercivity claim",
    "unrestricted Chronos-RR claim",
    "H4.1/FGL claim",
    "P vs NP claim",
    "Clay-problem claim",
    "empirical-validation claim",
    "No source rewrite is required",
    "`NO_CHANGE`",
]

FORBIDDEN_REVIEW = [
    "proves the Riemann Hypothesis",
    "solves the Riemann Hypothesis",
    "proves Euler-Gram coercivity",
    "solves any Clay problem",
    "proves Chronos-RR",
    "proves H4.1/FGL",
    "proves P vs NP",
    "theorem closure achieved",
]


def test_page_20_extract_tokens():
    text = PAGE.read_text()
    for token in REQUIRED_PAGE:
        assert token in text, token


def test_page_20_review_tokens():
    text = REVIEW.read_text()
    for token in REQUIRED_REVIEW:
        assert token in text, token


def test_page_20_review_no_forbidden_promotions():
    text = REVIEW.read_text()
    for token in FORBIDDEN_REVIEW:
        assert token not in text, token


def test_page_20_plan_updated():
    text = PLAN.read_text()
    assert "| 20 | `docs/page_audits/v0.1.2/page_20.txt` | NO_CHANGE |" in text
    assert "docs/page_audits/v0.1.2/reviews/page_20_review.md" in text
