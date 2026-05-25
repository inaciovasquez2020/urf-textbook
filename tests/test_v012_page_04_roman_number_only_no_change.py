from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_4_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_4.txt"

def test_page_04_extract_is_roman_number_only():
    assert EXTRACT.read_text(errors="ignore").strip() == "ii"

def test_page_04_review_records_no_change():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "Page 4 contains only the extracted roman page marker `ii`",
        "No content update is required for page 4",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_04_plan_row_records_no_change():
    text = PLAN.read_text()
    assert "| 4 | `docs/page_audits/v0.1.2/page_4.txt` | NO_CHANGE |" in text
    assert "page_4_review.md" in text
