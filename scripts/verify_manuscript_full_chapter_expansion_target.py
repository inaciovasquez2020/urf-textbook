#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ARTIFACT = ROOT / "artifacts/manuscript/manuscript_full_chapter_expansion_target_2026_05_20.json"
STATUS_DOC = ROOT / "docs/status/MANUSCRIPT_FULL_CHAPTER_EXPANSION_TARGET_2026_05_20.md"

REQUIRED_CHAPTERS = [
    "00_preface.tex",
    "01_foundations.tex",
    "02_refinement_locality.tex",
    "03_core_lemmas.tex",
    "04_main_theorems.tex",
    "05_examples_sat.tex",
    "06_examples_ym.tex",
    "07_examples_rh.tex",
    "08_examples_ns.tex",
    "09_examples_exchange.tex",
]

REQUIRED_BOUNDARY_TOKENS = [
    "does not complete the textbook",
    "does not prove a new theorem",
    "does not close Chronos-RR",
    "does not close H4.1/FGL",
    "does not prove P vs NP",
    "does not prove any Clay problem",
]

def fail(msg: str) -> int:
    print(f"MANUSCRIPT_FULL_CHAPTER_EXPANSION_TARGET failed: {msg}")
    return 1

def main() -> int:
    if not ARTIFACT.exists():
        return fail("missing artifact")
    if not STATUS_DOC.exists():
        return fail("missing status doc")

    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    if data.get("id") != "MANUSCRIPT_FULL_CHAPTER_EXPANSION_TARGET":
        return fail("artifact id mismatch")

    if data.get("status") != "TEXTBOOK_MANUSCRIPT_INCOMPLETE_FULL_EXPANSION_TARGET_DEFINED":
        return fail("artifact status mismatch")

    if "MANUSCRIPT_CHAPTER_COMPLETENESS_AUDIT" not in data.get("depends_on", []):
        return fail("missing dependency on chapter completeness audit")

    targets = data.get("chapter_targets", {})
    for chapter in REQUIRED_CHAPTERS:
        if chapter not in targets:
            return fail(f"missing chapter target: {chapter}")
        if len(targets[chapter]) < 4:
            return fail(f"chapter target too weak: {chapter}")

    gate = data.get("completion_gate", {})
    if gate.get("minimum_nonempty_lines_per_chapter") != 80:
        return fail("minimum nonempty line gate mismatch")
    if gate.get("minimum_sections_per_chapter") != 4:
        return fail("minimum section gate mismatch")
    if gate.get("minimum_theorem_style_blocks_per_chapter") != 2:
        return fail("minimum theorem-style block gate mismatch")
    if gate.get("requires_boundary_statement") is not True:
        return fail("missing boundary requirement")
    if gate.get("requires_exercises_or_review_prompts") is not True:
        return fail("missing exercises/review requirement")

    artifact_text = ARTIFACT.read_text(encoding="utf-8")
    status_text = STATUS_DOC.read_text(encoding="utf-8")

    for token in REQUIRED_BOUNDARY_TOKENS:
        if token not in artifact_text:
            return fail(f"artifact missing boundary token: {token}")
        if token not in status_text:
            return fail(f"status doc missing boundary token: {token}")

    for token in [
        "TEXTBOOK_MANUSCRIPT_INCOMPLETE_FULL_EXPANSION_TARGET_DEFINED",
        "full chapter expansion",
        "at least 80 nonempty lines per chapter",
        "at least 4 sections per chapter",
        "at least 2 theorem-style blocks per chapter",
    ]:
        if token not in status_text:
            return fail(f"status doc missing token: {token}")

    print("MANUSCRIPT_FULL_CHAPTER_EXPANSION_TARGET verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
