from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_18.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_18_review.md"

REQUIRED_REVIEW = [
    "v0.1.2 Page 18 Review",
    "Status: `NO_CHANGE`",
    "Extract: `docs/page_audits/v0.1.2/page_18.txt`",
    "continuation page",
    "v0.1.2 textbook audit sequence",
    "does not introduce a new theorem-closure claim",
    "unrestricted Chronos-RR claim",
    "H4.1/FGL claim",
    "P vs NP claim",
    "Clay-problem claim",
    "Yang-Mills mass-gap claim",
    "empirical-validation claim",
    "No source rewrite is required",
    "`NO_CHANGE`",
]

FORBIDDEN_REVIEW = [
    "proves Chronos-RR",
    "proves H4.1/FGL",
    "proves P vs NP",
    "solves any Clay problem",
    "proves Yang-Mills",
    "proves the Yang-Mills mass gap",
    "empirical validation achieved",
    "theorem closure achieved",
]


def test_page_18_extract_exists():
    assert PAGE.exists()
    assert PAGE.read_text().strip()


def test_page_18_review_tokens():
    text = REVIEW.read_text()
    for token in REQUIRED_REVIEW:
        assert token in text, token


def test_page_18_review_no_forbidden_promotions():
    text = REVIEW.read_text()
    for token in FORBIDDEN_REVIEW:
        assert token not in text, token


def test_page_18_plan_updated():
    text = PLAN.read_text()
    assert "| 18 | `docs/page_audits/v0.1.2/page_18.txt` | NO_CHANGE |" in text
    assert "docs/page_audits/v0.1.2/reviews/page_18_review.md" in text
