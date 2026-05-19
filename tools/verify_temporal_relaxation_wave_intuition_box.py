from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/notes/TEMPORAL_RELAXATION_WAVE_INTUITION_BOX_2026_05_18.md"
README = ROOT / "README.md"

required = [
    "Status: `TEXTBOOK_INTUITION_BOX_ONLY`",
    "TemporalRelaxationWave",
    "W(t)=A e^{-\\lambda t}\\sin(\\omega t+\\phi)",
    "E_{\\mathrm{inst}}(t)",
    "E_{\\mathrm{env}}(t)",
    "E_{\\mathrm{inst}}(t)\\le E_{\\mathrm{env}}(0)e^{-2\\lambda t}",
    "Disturbance Recovery Example",
    "This is a textbook intuition box only.",
    "It may be connected to URF only if later upgraded",
]

forbidden = [
    "proves URF",
    "proves Chronos-RR",
    "proves H4.1/FGL",
    "UniversalFiberEntropyGap is proved",
    "P vs NP is solved",
    "Clay problem is solved",
    "theorem-level closure",
]

def main() -> None:
    text = DOC.read_text()

    for token in required:
        assert token in text, f"missing required token: {token}"

    for token in forbidden:
        assert token not in text, f"forbidden overclaim token present: {token}"

    if README.exists():
        readme = README.read_text()
        assert "TEMPORAL_RELAXATION_WAVE_INTUITION_BOX_2026_05_18.md" in readme

    print("Temporal relaxation wave intuition box verified.")

if __name__ == "__main__":
    main()
