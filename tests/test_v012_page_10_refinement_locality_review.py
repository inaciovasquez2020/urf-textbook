from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_10.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_10_review.md"
SOURCE = ROOT / "manuscript/chapters/02_refinement_locality.tex"

def test_page_10_extract_is_chapter_opening():
    text = PAGE.read_text().upper()
    assert "CHAPTER 2" in text
    assert "REFINEMENT AND LOCALITY" in text

def test_page_10_review_records_no_change_boundary():
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "CHAPTER 2. REFINEMENT AND LOCALITY",
        "`manuscript/chapters/02_refinement_locality.tex`",
        "No PDF source text was modified",
        "No release metadata or mathematical clarification is required",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_10_plan_row_marked_no_change():
    text = PLAN.read_text()
    assert "| 10 | `docs/page_audits/v0.1.2/page_10.txt` | NO_CHANGE |" in text
    assert "page_10_review.md" in text

def test_page_10_source_contains_refinement_locality_title():
    text = SOURCE.read_text()
    assert "Refinement and Locality" in text or "REFINEMENT AND LOCALITY" in text
