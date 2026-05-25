from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_2_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_2.txt"

def test_page_02_extract_is_number_only():
    assert EXTRACT.read_text(errors="ignore").strip() == "2"

def test_page_02_review_records_no_change():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "Page 2 contains only the extracted page marker `2`",
        "No content update is required for page 2",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_02_plan_row_records_no_change():
    text = PLAN.read_text()
    assert "| 2 | `docs/page_audits/v0.1.2/page_2.txt` | NO_CHANGE |" in text
    assert "page_2_review.md" in text
