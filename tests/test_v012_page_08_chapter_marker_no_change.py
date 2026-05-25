from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_8_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_8.txt"

def test_page_08_extract_is_chapter_marker_only():
    assert EXTRACT.read_text(errors="ignore").strip() == "2CHAPTER 1. FOUNDATIONS"

def test_page_08_review_records_no_change():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "Page 8 contains only the extracted chapter continuation marker",
        "No content update is required for page 8",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_08_plan_row_records_no_change():
    text = PLAN.read_text()
    assert "| 8 | `docs/page_audits/v0.1.2/page_8.txt` | NO_CHANGE |" in text
    assert "page_8_review.md" in text
