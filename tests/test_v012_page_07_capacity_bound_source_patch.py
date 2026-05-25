from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
PATCH = ROOT / "docs/page_audits/v0.1.2/reviews/page_7_source_patch.md"

def test_page_07_source_patch_review_exists():
    assert PATCH.exists()
    text = PATCH.read_text()
    required = [
        "Status: `BOUNDARY_CLARIFICATION`",
        "Source patched: `journal/urf_core.tex`",
        "Added a local context note",
        "exposition-level organizing invariant",
        "buildable formal source repository artifact",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_07_plan_row_records_source_patch():
    text = PLAN.read_text()
    assert "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | BOUNDARY_CLARIFICATION |" in text
    assert "page_7_source_patch.md" in text

def test_page_07_source_contains_context_note():
    text = PATCH.read_text()
    marker = "Source patched: `"
    start = text.index(marker) + len(marker)
    end = text.index("`", start)
    source = ROOT / text[start:end]
    source_text = source.read_text(errors="ignore")
    required = [
        "The capacity bound on this page is an exposition-level organizing invariant for the textbook.",
        "not as an independent proof of any unrestricted theorem",
        "the source of truth is the corresponding buildable formal repository artifact",
    ]
    for token in required:
        assert token in source_text, token
