from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "docs/foundations/FRONTIER_CALCULUS.md": [
        "Status: Doctrine / Repository-Governance Layer",
        "Completion is not identical to solution.",
        "Completion means the remaining gap has been made exact.",
        "NEGATIVE_CLOSURE_CERTIFICATE.json",
        "Forbidden Transition",
    ],
    "docs/status/FRONTIER_CALCULUS_ADOPTION.md": [
        "Status: Adopted as a documentation and audit pattern.",
        "This file does not claim that any open theorem is solved.",
        "closed executable surface",
        "certified frontier",
        "open mathematical obstruction",
    ],
}

def main() -> None:
    for rel, needles in REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"missing required file: {rel}")
        text = path.read_text()
        for needle in needles:
            if needle not in text:
                raise SystemExit(f"missing required text in {rel}: {needle}")
    print("frontier calculus doctrine verified")

if __name__ == "__main__":
    main()
