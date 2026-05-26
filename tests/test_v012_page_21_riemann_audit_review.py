from pathlib import Path

PLAN = Path("docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md")
REVIEW = Path("docs/page_audits/v0.1.2/reviews/page_21_review.md")

REQUIRED_REVIEW = [
    "v0.1.2 Page 21 Review",
    "docs/page_audits/v0.1.2/page_21.txt",
    "Riemann Hypothesis",
    "Euler-Gram coercivity",
    "unrestricted Chronos-RR",
    "H4.1/FGL",
    "P vs NP",
    "any Clay problem",
    "empirical-validation claim",
]

FORBIDDEN_REVIEW = [
    "proves the Riemann Hypothesis",
    "proves Euler-Gram coercivity",
    "theorem closure achieved",
    "unrestricted Chronos-RR proved",
    "H4.1/FGL proved",
    "P vs NP proved",
    "Clay problem solved",
    "empirical validation achieved",
]


def test_page_21_review_exists():
    assert REVIEW.exists()


def test_page_21_review_tokens():
    text = REVIEW.read_text()
    for token in REQUIRED_REVIEW:
        assert token in text, token


def test_page_21_review_no_forbidden_promotions():
    text = REVIEW.read_text()
    for token in FORBIDDEN_REVIEW:
        assert token not in text, token


def test_page_21_plan_updated():
    text = PLAN.read_text()
    assert "| 21 | `docs/page_audits/v0.1.2/page_21.txt` |" in text
    assert "docs/page_audits/v0.1.2/reviews/page_21_review.md" in text
