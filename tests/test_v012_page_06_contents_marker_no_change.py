from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_6_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_6.txt"

def test_page_06_extract_is_contents_marker_only():
    assert EXTRACT.read_text(errors="ignore").strip() == "iv CONTENTS"

def test_page_06_review_records_no_change():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "Page 6 contains only the extracted continuation marker `iv CONTENTS`",
        "No content update is required for page 6",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_06_plan_row_records_no_change():
    text = PLAN.read_text()
    assert "| 6 | `docs/page_audits/v0.1.2/page_6.txt` | NO_CHANGE |" in text
    assert "page_6_review.md" in text
