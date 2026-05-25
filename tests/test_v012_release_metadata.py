from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "releases/v0.1.2/urf-textbook-v0.1.2.pdf",
    ROOT / "releases/v0.1.2/SHA256.txt",
    ROOT / "releases/v0.1.2/README.md",
    ROOT / "docs/release_notes/v0.1.2.md",
    ROOT / "CHANGELOG.md",
]

REQUIRED_TOKENS = [
    "v0.1.2",
    "Infrastructure consolidation release",
    "b4704ca9a791346585826a02dc1baf184c0d6f7f6e7fd9a3aedda0bfc2ef059e",
    "Documentation/release metadata only",
    "Does not prove:",
    "unrestricted Chronos-RR",
    "unrestricted H4.1/FGL",
    "P vs NP",
    "any Clay problem",
]

def test_v012_release_metadata_files_exist():
    for path in REQUIRED_FILES:
        assert path.exists(), str(path)

def test_v012_release_metadata_contains_boundary_tokens():
    combined = "\n".join(
        path.read_text(errors="ignore")
        for path in [
            ROOT / "releases/v0.1.2/README.md",
            ROOT / "docs/release_notes/v0.1.2.md",
            ROOT / "CHANGELOG.md",
        ]
    )
    for token in REQUIRED_TOKENS:
        assert token in combined, token
