from pathlib import Path

PLAN = Path("docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md")
REVIEW = Path("docs/page_audits/v0.1.2/reviews/page_31_review.md")

REQUIRED_REVIEW = [
    "v0.1.2 Page 31 Review",
    "docs/page_audits/v0.1.2/page_31.txt",
    "References / bibliography",
    "citation metadata",
    "theorem closure",
    "unrestricted Chronos-RR",
    "H4.1/FGL",
    "P vs NP",
    "any Clay problem",
    "empirical-validation claim",
    "`NO_CHANGE`",
]

FORBIDDEN_REVIEW = [
    "proves a theorem closure",
    "theorem closure achieved",
    "unrestricted Chronos-RR proved",
    "H4.1/FGL proved",
    "P vs NP proved",
    "Clay problem solved",
    "empirical validation achieved",
]


def test_page_31_review_exists():
    assert REVIEW.exists()


def test_page_31_review_tokens():
    text = REVIEW.read_text()
    for token in REQUIRED_REVIEW:
        assert token in text, token


def test_page_31_review_no_forbidden_promotions():
    text = REVIEW.read_text()
    for token in FORBIDDEN_REVIEW:
        assert token not in text, token


def test_page_31_plan_updated():
    text = PLAN.read_text()
    assert "| 31 | `docs/page_audits/v0.1.2/page_31.txt` | NO_CHANGE |" in text
    assert "docs/page_audits/v0.1.2/reviews/page_31_review.md" in text
