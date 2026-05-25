from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_12.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_12_review.md"
SOURCE = ROOT / "manuscript/chapters/03_core_lemmas.tex"

def test_page_12_extract_is_core_lemmas_page_mark():
    text = PAGE.read_text().upper()
    assert "CHAPTER 3. CORE LEMMAS" in text

def test_page_12_review_records_no_change_boundary():
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "CHAPTER 3. CORE LEMMAS",
        "does not contain a theorem statement",
        "`manuscript/chapters/03_core_lemmas.tex`",
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

def test_page_12_plan_row_marked_no_change():
    text = PLAN.read_text()
    assert "| 12 | `docs/page_audits/v0.1.2/page_12.txt` | NO_CHANGE |" in text
    assert "page_12_review.md" in text

def test_page_12_source_contains_core_lemmas_title():
    text = SOURCE.read_text()
    assert "Core Lemmas" in text
