from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs/page_audits/v0.1.2/page_11.txt"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_11_review.md"
SOURCE = ROOT / "manuscript/chapters/03_core_lemmas.tex"

def test_page_11_extract_is_core_lemmas_chapter_opening():
    text = PAGE.read_text()
    assert "Chapter 3" in text
    assert "Core Lemmas" in text
    assert "non-amplification" in text
    assert "capacity additivity" in text
    assert "sequential decomposition" in text
    assert "spectral floor" in text

def test_page_11_review_records_no_change_boundary():
    text = REVIEW.read_text()
    required = [
        "Status: `NO_CHANGE`",
        "Chapter 3 — Core Lemmas",
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

def test_page_11_plan_row_marked_no_change():
    text = PLAN.read_text()
    assert "| 11 | `docs/page_audits/v0.1.2/page_11.txt` | NO_CHANGE |" in text
    assert "page_11_review.md" in text

def test_page_11_source_contains_core_lemmas_material():
    text = SOURCE.read_text()
    assert "Core Lemmas" in text
    assert (
        "non-amplification" in text
        or "capacity additivity" in text
        or "sequential decomposition" in text
        or "spectral floor" in text
    )
