#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTERS = [
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

MIN_NONEMPTY_LINES = 12
FORBIDDEN = [
    "TODO",
    "PLACEHOLDER",
    "This chapter is incomplete.",
    "add below as needed"
]

def fail(message: str) -> int:
    print(f"MANUSCRIPT_CHAPTER_COMPLETENESS_AUDIT failed: {message}")
    return 1

def brace_balance(text: str) -> bool:
    stripped = re.sub(r"\\[{}]", "", text)
    return stripped.count("{") == stripped.count("}")

def main() -> int:
    artifact = ROOT / "artifacts/manuscript/manuscript_chapter_completeness_audit_2026_05_20.json"
    status_doc = ROOT / "docs/status/MANUSCRIPT_CHAPTER_COMPLETENESS_AUDIT_2026_05_20.md"
    main_tex = ROOT / "manuscript/main.tex"

    if not artifact.exists():
        return fail("missing audit artifact")
    if not status_doc.exists():
        return fail("missing status doc")
    if not main_tex.exists():
        return fail("missing manuscript/main.tex")

    artifact_data = json.loads(artifact.read_text(encoding="utf-8"))
    if artifact_data.get("id") != "MANUSCRIPT_CHAPTER_COMPLETENESS_AUDIT":
        return fail("artifact id mismatch")
    if artifact_data.get("status") != "TEXTBOOK_MANUSCRIPT_INCOMPLETE":
        return fail("artifact status mismatch")

    status_text = status_doc.read_text(encoding="utf-8")
    for token in [
        "MANUSCRIPT_CHAPTER_COMPLETENESS_AUDIT",
        "TEXTBOOK_MANUSCRIPT_INCOMPLETE",
        "does not make the textbook complete",
        "does not prove P vs NP",
        "does not prove any Clay problem",
    ]:
        if token not in status_text:
            return fail(f"status doc missing token: {token}")

    main_text = main_tex.read_text(encoding="utf-8")
    for chapter in CHAPTERS:
        include = f"\\input{{manuscript/chapters/{chapter}}}"
        if include not in main_text:
            return fail(f"main.tex does not include {chapter}")

    for chapter in CHAPTERS:
        path = ROOT / "manuscript/chapters" / chapter
        if not path.exists():
            return fail(f"missing chapter: {chapter}")

        text = path.read_text(encoding="utf-8")
        lines = [line for line in text.splitlines() if line.strip()]

        if len(lines) < MIN_NONEMPTY_LINES:
            return fail(f"{chapter} has only {len(lines)} nonempty lines")

        if "\\chapter" not in text:
            return fail(f"{chapter} missing chapter declaration")

        if chapter != "00_preface.tex" and "\\section" not in text:
            return fail(f"{chapter} missing section declaration")

        if not any(env in text for env in [
            "\\begin{definition}",
            "\\begin{lemma}",
            "\\begin{theorem}",
            "\\begin{example}",
            "\\begin{remark}",
        ]):
            return fail(f"{chapter} missing theorem-style environment")

        upper = text.upper()
        for token in FORBIDDEN:
            if token in upper:
                return fail(f"{chapter} contains forbidden placeholder token: {token}")

        if re.search(r"T_\{\s*$", text):
            return fail(f"{chapter} contains truncated T_{{ expression")

        if not brace_balance(text):
            return fail(f"{chapter} has unbalanced braces")

    foundations = (ROOT / "manuscript/chapters/01_foundations.tex").read_text(encoding="utf-8")
    if r"I(X;T_t \mid T_{t-1}) \le C_t" not in foundations:
        return fail("01_foundations.tex missing repaired capacity expression")

    print("MANUSCRIPT_CHAPTER_COMPLETENESS_AUDIT verified.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
