from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_7_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_7.txt"

def test_page_07_extract_is_substantive_foundations_page():
    text = EXTRACT.read_text(errors="ignore")
    required = [
        "Chapter 1",
        "Foundations",
        "Transcript-Limited Refinement",
        "Capacity Bound",
        "I(X;",
    ]
    for token in required:
        assert token in text, token

def test_page_07_review_records_missing_context():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `MISSING_CONTEXT`",
        "first substantive mathematical page",
        "extracted formula appears incomplete",
        "Required Next Object",
        "verify the complete capacity-bound statement",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_07_plan_row_records_missing_context():
    text = PLAN.read_text()
    assert "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | MISSING_CONTEXT |" in text
    assert "page_7_review.md" in text
