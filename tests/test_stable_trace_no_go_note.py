from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def test_stable_trace_no_go_note_doc():
    text = (ROOT / "docs/theorems/STABLE_TRACE_NO_GO.md").read_text()
    assert "Status: `EXTERNAL_READABLE_NOTE / REFUTED_UNCONDITIONAL_TARGET`" in text
    assert "[Inhabited X.Trace]" in text
    assert "Generator := Unit" in text
    assert "Trace := Empty" in text
    assert "urf-core PR #341" in text
    assert "main commit f1f28fa" in text


def test_stable_trace_no_go_note_boundary():
    text = (ROOT / "docs/theorems/STABLE_TRACE_NO_GO.md").read_text()
    assert "This note does not prove:" in text
    assert "- unconditional `StableTraceCertificateExists`" in text
    assert "- unconditional `StableGenAdmissibleTrace`" in text
    assert "- unrestricted `UniversalFiberEntropyGap`" in text
    assert "- unrestricted Chronos-RR" in text
    assert "- unrestricted H4.1/FGL" in text
    assert "- P vs NP" in text
    assert "- any Clay problem" in text


def test_stable_trace_no_go_note_artifact():
    data = json.loads((ROOT / "artifacts/textbook/stable_trace_no_go_note_2026_05_19.json").read_text())
    assert data["status"] == "EXTERNAL_READABLE_NOTE / REFUTED_UNCONDITIONAL_TARGET"
    assert data["source_repo"] == "urf-core"
    assert data["source_pr"] == 341
    assert data["source_commit"] == "f1f28fa"
    assert len(data["countermodels"]) == 2
