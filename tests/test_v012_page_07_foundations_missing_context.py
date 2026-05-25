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

def test_page_07_initial_review_file_records_missing_context():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    assert "Status: `MISSING_CONTEXT`" in text
    assert "page 7" in text.lower()

def test_page_07_plan_row_is_reviewed_or_promoted():
    text = PLAN.read_text()
    assert "| 7 | `docs/page_audits/v0.1.2/page_7.txt` |" in text
    assert (
        "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | MISSING_CONTEXT |" in text
        or "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | BOUNDARY_CLARIFICATION |" in text
        or "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | SOURCE_OR_RELEASE_METADATA_NEEDED |" in text
    )
