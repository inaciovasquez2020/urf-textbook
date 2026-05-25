from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
PATCH = ROOT / "docs/page_audits/v0.1.2/reviews/page_7_source_patch.md"

def test_page_07_source_patch_attempt_records_latex_blocker():
    assert PATCH.exists()
    text = PATCH.read_text()
    required = [
        "Status: `SOURCE_OR_RELEASE_METADATA_NEEDED`",
        "source location was identified as `journal/urf_core.tex`",
        "initial source-context edit caused the LaTeX Build workflow to fail",
        "source edit was reverted",
        "Required Next Object",
        "LaTeX-build-safe source-context note",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_07_plan_row_records_latex_blocker():
    text = PLAN.read_text()
    assert "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | SOURCE_OR_RELEASE_METADATA_NEEDED |" in text
    assert "page_7_source_patch.md" in text
