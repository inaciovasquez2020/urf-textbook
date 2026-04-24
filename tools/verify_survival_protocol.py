from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/SURVIVAL_PROTOCOL.md"

REQUIRED = [
    "Status: Repository-governance protocol",
    "solved theorem",
    "closed executable surface",
    "certified frontier",
    "conditional result",
    "open obstruction",
    "A repository must not imply that an open theorem is solved",
    "conversion of unfinished research into auditable frontier-normalized artifacts",
    "Continue only by consolidation",
]

def main() -> None:
    if not DOC.exists():
        raise SystemExit("missing docs/status/SURVIVAL_PROTOCOL.md")
    text = DOC.read_text()
    for needle in REQUIRED:
        if needle not in text:
            raise SystemExit(f"missing required text: {needle}")
    print("survival protocol verified")

if __name__ == "__main__":
    main()
