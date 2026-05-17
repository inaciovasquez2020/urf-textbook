from pathlib import Path

DOC = Path("docs/dreams/DREAMS_MATH.md")
INDEX = Path("docs/index/DOCUMENTATION_INDEX.md")
ROADMAP = Path("ROADMAP.md")

required = [
    "Status: CONDITIONAL_EXPOSITION_FRONTIER",
    "It is not a theorem layer.",
    "Pointwise positivity is insufficient.",
    "UniversalFiberEntropyGap requires a single uniform positive lower bound.",
    "does not prove Cosmic Censorship",
    "does not prove:",
    "unrestricted UniversalFiberEntropyGap",
    "unrestricted Chronos-RR",
    "unrestricted H4.1/FGL",
    "P vs NP",
    "any Clay problem",
]

for path in [DOC, INDEX, ROADMAP]:
    assert path.exists(), f"missing {path}"

doc = DOC.read_text()
for token in required:
    assert token in doc, f"missing token: {token}"

assert "docs/dreams/DREAMS_MATH.md" in INDEX.read_text()
assert "Dreams Math" in ROADMAP.read_text()

forbidden = [
    "proves P vs NP",
    "solves P vs NP",
    "proves Cosmic Censorship",
    "proves the Hoop Conjecture",
    "proves unrestricted UniversalFiberEntropyGap",
    "proves unrestricted Chronos-RR",
    "proves unrestricted H4.1/FGL",
    "solves any Clay problem",
    "unconditional final proof",
]

lower = doc.lower()
for phrase in forbidden:
    assert phrase.lower() not in lower, f"forbidden promotion phrase: {phrase}"

print("Dreams Math exposition frontier verified.")
