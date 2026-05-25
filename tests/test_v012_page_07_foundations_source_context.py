from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "manuscript/chapters/01_foundations.tex"
PLAN = ROOT / "docs/page_audits/v0.1.2/PAGE_BY_PAGE_UPDATE_PLAN.md"
REVIEW = ROOT / "docs/page_audits/v0.1.2/reviews/page_7_source_context.md"

def test_page_07_source_context_exists():
    text = SOURCE.read_text()
    assert "v0.1.2 page 7 source context:" in text
    assert "I(X;T_t \\mid T_{t-1}) \\le C_t" in text
    assert "does not promote theorem status" in text

def test_page_07_source_context_review_records_boundary():
    text = REVIEW.read_text()
    required = [
        "Status: `BOUNDARY_CLARIFICATION`",
        "`manuscript/chapters/01_foundations.tex`",
        "I(X;T_t \\mid T_{t-1}) \\le C_t",
        "No mathematical theorem statement was strengthened",
        "Does not prove:",
        "unrestricted Chronos-RR",
        "unrestricted H4.1/FGL",
        "P vs NP",
        "any Clay problem",
    ]
    for token in required:
        assert token in text, token

def test_page_07_plan_row_promoted_to_boundary_clarification():
    text = PLAN.read_text()
    assert "| 7 | `docs/page_audits/v0.1.2/page_7.txt` | BOUNDARY_CLARIFICATION |" in text
    assert "page_7_source_context.md" in text

def test_page_07_source_context_is_comment_only():
    text = SOURCE.read_text()
    start = text.index("% v0.1.2 page 7 source context:")
    lines = text[start:].splitlines()
    comment_lines = []
    for line in lines:
        if line.startswith("%"):
            comment_lines.append(line)
            continue
        break
    block = "\\n".join(comment_lines)
    assert comment_lines
    assert all(line.startswith("%") for line in comment_lines)
    assert "\\begin{theorem}" not in block
    assert "\\begin{lemma}" not in block
