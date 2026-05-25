from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript/main.tex"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_3_release_identifier.md"

def test_page_03_title_source_contains_release_identifier():
    text = SOURCE.read_text()
    assert "Unified Rigidity Framework Textbook" in text
    assert "Release: v0.1.2" in text

def test_page_03_release_identifier_review_records_boundary():
    text = REVIEW.read_text()
    required = [
        "Status: `BOUNDARY_CLARIFICATION`",
        "`manuscript/main.tex`",
        "Release: v0.1.2",
        "No mathematical theorem statement was strengthened",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_03_plan_row_promoted_to_boundary_clarification():
    text = PLAN.read_text()
    assert "| 3 | `docs/page_audits/v0.1.2/page_3.txt` | BOUNDARY_CLARIFICATION |" in text
    assert "page_3_release_identifier.md" in text
