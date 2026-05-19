from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

doc = ROOT / "docs/theorems/STABLE_TRACE_NO_GO.md"
artifact = ROOT / "artifacts/textbook/stable_trace_no_go_note_2026_05_19.json"

doc_text = doc.read_text()
data = json.loads(artifact.read_text())

required_doc = [
    "Status: `EXTERNAL_READABLE_NOTE / REFUTED_UNCONDITIONAL_TARGET`",
    "For an arbitrary URF capacity interface",
    "The valid equivalence requires inhabited traces",
    "[Inhabited X.Trace]",
    "Generator := Unit",
    "Trace := Empty",
    "StableGen := fun _ => False",
    "StableGen := fun _ => True",
    "Unit → Empty",
    "urf-core PR #341",
    "main commit f1f28fa",
    "This note does not prove:",
    "unconditional `StableTraceCertificateExists`",
    "unconditional `StableGenAdmissibleTrace`",
    "unrestricted `UniversalFiberEntropyGap`",
    "unrestricted Chronos-RR",
    "unrestricted H4.1/FGL",
    "P vs NP",
    "any Clay problem",
]

for token in required_doc:
    assert token in doc_text, token

assert data["status"] == "EXTERNAL_READABLE_NOTE / REFUTED_UNCONDITIONAL_TARGET"
assert data["source_repo"] == "urf-core"
assert data["source_pr"] == 341
assert data["source_commit"] == "f1f28fa"
assert "Inhabited X.Trace" in data["surviving_statement"]
assert len(data["countermodels"]) == 2

for forbidden in [
    "solves P vs NP",
    "proves P vs NP",
    "solves any Clay problem",
    "proves any Clay problem",
    "unrestricted Chronos-RR is proved",
    "unrestricted UniversalFiberEntropyGap is proved",
]:
    assert forbidden not in doc_text

print("Stable trace no-go note verified.")
