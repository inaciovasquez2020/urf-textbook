from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_5_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_5.txt"

def test_page_05_extract_is_contents_page():
    text = EXTRACT.read_text(errors="ignore")
    required = [
        "Contents",
        "Preface",
        "Foundations",
        "Core Lemmas",
        "Main Theorems",
        "Lean Formalization Map",
        "Certificate Schema",
        "Normalization Taxonomy",
    ]
    for token in required:
        assert token in text, token

def test_page_05_review_records_no_change():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "Page 5 is the table of contents",
        "The page is navigational only",
        "No content update is required for page 5",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_05_plan_row_records_no_change():
    text = PLAN.read_text()
    assert "| 5 | `docs/page_audits/v0.1.2/page_5.txt` | NO_CHANGE |" in text
    assert "page_5_review.md" in text
