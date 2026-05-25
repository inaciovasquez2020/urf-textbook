from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_3_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_3.txt"

def test_page_03_extract_is_title_page():
    text = EXTRACT.read_text(errors="ignore")
    required = [
        "Unified Rigidity Framework Textbook",
        "Capacity, Locality, and Terminal Obstructions",
        "Inacio Vasquez",
        "March 1, 2026",
    ]
    for token in required:
        assert token in text, token

def test_page_03_review_records_release_metadata_gap():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `SOURCE_OR_RELEASE_METADATA_NEEDED`",
        "Page 3 is the title page",
        "does not explicitly identify the frozen release version `v0.1.2`",
        "Release: v0.1.2",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_03_plan_row_records_release_metadata_gap_or_closure():
    text = PLAN.read_text()
    assert "| 3 | `docs/page_audits/v0.1.2/page_3.txt` |" in text
    assert (
        "| 3 | `docs/page_audits/v0.1.2/page_3.txt` | SOURCE_OR_RELEASE_METADATA_NEEDED |" in text
        or "| 3 | `docs/page_audits/v0.1.2/page_3.txt` | BOUNDARY_CLARIFICATION |" in text
    )
    assert (
        "page_3_review.md" in text
        or "page_3_release_identifier.md" in text
    )
