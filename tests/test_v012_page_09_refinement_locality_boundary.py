from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_9_review.md"
EXTRACT = ROOT / "docs/page_audits/v0.1.2/page_9.txt"

def test_page_09_extract_is_substantive_refinement_locality_page():
    text = EXTRACT.read_text(errors="ignore")
    required = [
        "Chapter 2",
        "Refinement and Locality",
        "bounded transcript capacity",
        "admissible refinement operators",
        "locality constraints",
        "normalization principle",
        "polynomial-time algorithms",
        "bounded-width refinement sequences",
        "Information Gain per Step",
    ]
    for token in required:
        assert token in text, token

def test_page_09_review_records_boundary_clarification():
    assert REVIEW.exists()
    text = REVIEW.read_text()
    required = [
        "Status: `BOUNDARY_CLARIFICATION`",
        "substantive mathematical exposition",
        "algorithmic normalization",
        "Required Next Object",
        "buildable formal source repository artifact",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_09_plan_row_records_boundary_clarification():
    text = PLAN.read_text()
    assert "| 9 | `docs/page_audits/v0.1.2/page_9.txt` | BOUNDARY_CLARIFICATION |" in text
    assert "page_9_review.md" in text
