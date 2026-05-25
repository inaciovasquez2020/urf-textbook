from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"

def test_v012_page_by_page_plan_exists():
    assert PLAN.exists()

def test_v012_page_by_page_plan_has_boundary_tokens():
    text = PLAN.read_text()
    required = [
        "URF Textbook v0.1.2 Page-by-Page Update Plan",
        "Status: page-by-page audit scaffold only",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
        "No theorem-level claim may be promoted from this audit",
    ]
    for token in required:
        assert token in text, token

def test_v012_page_extracts_exist():
    text = PLAN.read_text()
    page_lines = [line for line in text.splitlines() if line.startswith("| ") and "page_" in line]
    assert page_lines, "no page rows found"
    for line in page_lines:
        start = line.index("`") + 1
        end = line.index("`", start)
        path = ROOT / line[start:end]
        assert path.exists(), line
        assert path.read_text(errors="ignore").strip() != "", line
