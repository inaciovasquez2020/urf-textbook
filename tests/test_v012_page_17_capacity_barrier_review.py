from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_17.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_17_review.md"

REQUIRED_PAGE = [
    "Example: Yang–Mills",
    "spectral gap and mass-gap questions",
    "capacity barrier",
    "persistent modes",
]

REQUIRED_REVIEW = [
    "v0.1.2 Page 17 Review",
    "Status: `BOUNDARY_CLARIFICATION`",
    "Extract: `docs/page_audits/v0.1.2/page_17.txt`",
    "Yang-Mills example sentence",
    "interpretive framework language only",
    "textbook-level analogy",
    "spectral-gap/mass-gap questions",
    "transcript-capacity rigidity",
    "does not prove",
    "Yang-Mills existence",
    "Yang-Mills mass gap",
    "any Clay problem",
    "unrestricted Chronos-RR",
    "H4.1/FGL",
    "P vs NP",
    "theorem-level closure of the capacity-barrier principle",
    "No source rewrite is required",
    "`BOUNDARY_CLARIFICATION`",
]

FORBIDDEN_REVIEW = [
    "proves Yang-Mills",
    "proves the Yang-Mills mass gap",
    "solves Yang-Mills",
    "solves any Clay problem",
    "proves Chronos-RR",
    "proves H4.1/FGL",
    "proves P vs NP",
    "theorem closure achieved",
]


def test_page_17_extract_tokens():
    text = PAGE.read_text().replace("per-\nsistent", "persistent")
    for token in REQUIRED_PAGE:
        assert token in text, token


def test_page_17_review_tokens():
    text = REVIEW.read_text()
    for token in REQUIRED_REVIEW:
        assert token in text, token


def test_page_17_review_no_forbidden_promotions():
    text = REVIEW.read_text()
    for token in FORBIDDEN_REVIEW:
        assert token not in text, token


def test_page_17_plan_updated():
    text = PLAN.read_text()
    assert "| 17 | `docs/page_audits/v0.1.2/page_17.txt` | BOUNDARY_CLARIFICATION |" in text
    assert "docs/page_audits/v0.1.2/reviews/page_17_review.md" in text
