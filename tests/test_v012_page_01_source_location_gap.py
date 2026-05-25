from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_1_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_1.txt"

def test_page_01_review_records_source_location_gap():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `SOURCE_OR_RELEASE_METADATA_NEEDED`",
        "Global behavior is constrained by local capacity bounds",
        "source file that generated this page was not located",
        "Required Next Object",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_01_plan_row_records_source_location_gap():
    text = PLAN.read_text()
    assert "| 1 | `docs/page_audits/v0.1.2/page_1.txt` | SOURCE_OR_RELEASE_METADATA_NEEDED |" in text
    assert "page_1_review.md" in text

def test_page_01_extract_contains_preface_thesis():
    text = EXTRACT.read_text(errors="ignore")
    assert "Preface" in text
    assert "Global behavior is constrained by local capacity bounds" in text
