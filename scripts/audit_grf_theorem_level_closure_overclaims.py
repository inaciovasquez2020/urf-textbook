#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

FILES = [
    ROOT / "docs/essays/GRF_2026_PHYSICAL_REALIZATION_AND_FINAL_CLOSURE.md",
    ROOT / "docs/essays/GRF_2026_ALGEBRAIC_JET_MATCHING_THEOREM.md",
    ROOT / "docs/essays/GRF_2026_EXPLICIT_TRANSITION_SHELL_CERTIFICATE.md",
    ROOT / "artifacts/grf/physical_realization_theorem.json",
    ROOT / "artifacts/grf/grf_theorem_level_closure_certificate.json",
]

FORBIDDEN = [
    r"\bsolves\s+general\s+relativity\b",
    r"\bsolves\s+gravity\b",
    r"\bcomplete\s+theory\s+of\s+gravity\b",
    r"\bproves\s+cosmic\s+censorship\b",
    r"\bproves\s+the\s+hoop\s+conjecture\b",
    r"\bproves\s+dark\s+matter\b",
    r"\bproves\s+dark\s+energy\b",
    r"\bNobel(?:-|\s*)level\s+discovery\b",
    r"\bClay\s+problem\s+closure\b",
    r"\baccepted\s+by\s+physics\b",
    r"\bexternally\s+accepted\b",
    r"\bunrestricted\s+gravity\s+closure\b",
    r"\bfinal\s+physical\s+theory\b",
]

NEGATING_CONTEXT = re.compile(
    r"\b(does\s+not\s+prove|doesn't\s+prove|not\s+a\s+proof\s+of|no\s+claim\s+of|boundary:|does\s+not\s+establish|not\s+establish)\b",
    re.IGNORECASE,
)

def main() -> int:
    missing = [str(p.relative_to(ROOT)) for p in FILES if not p.exists()]
    if missing:
        print("Missing audited files:")
        for item in missing:
            print(f"- {item}")
        return 1

    failures = []
    for path in FILES:
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if NEGATING_CONTEXT.search(line):
                continue
            for pattern in FORBIDDEN:
                if re.search(pattern, line, flags=re.IGNORECASE):
                    failures.append((path.relative_to(ROOT), lineno, pattern, line.strip()))

    if failures:
        print("GRF theorem-level closure overclaim audit FAILED.")
        for rel, lineno, pattern, line in failures:
            print(f"{rel}:{lineno}: {pattern}: {line}")
        return 1

    print("GRF theorem-level closure overclaim audit OK.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
