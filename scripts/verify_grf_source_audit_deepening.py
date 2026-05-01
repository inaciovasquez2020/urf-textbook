#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT_DEEPENING.md")
text = path.read_text(encoding="utf-8")

required = [
    "Deep Source Audit",
    "Gordon optical metric",
    "Transformation optics and geometry of light",
    "Fabricated graded-index optics",
    "Energy conditions as admissibility filters",
    "Quantum inequalities and magnitude-duration limits",
    "Operational interpretation of negative energy",
    "Two-function anisotropic static metrics",
    "Exact anisotropic solutions satisfying energy conditions",
    "Global Matching Lemma",
    "It is not yet:",
    "A global Einstein-matter construction theorem.",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

source_tokens = [
    "gordon_-_optical_metrics.pdf",
    "0805.4778",
    "10.1016/S0079-6638(08)00202-3",
    "PMC9234043",
    "2003.01815",
    "gr-qc/9410043",
    "1208.5399",
    "gr-qc/9612029",
    "0712.0713",
    "0905.3546",
]

for token in source_tokens:
    if token not in text:
        raise SystemExit(f"missing source token: {token}")

forbidden = [
    "global einstein-matter construction theorem is proved",
    "semiclassical stability is proved",
    "finite capacity is established as standard",
    "solves gravity",
    "unconditional closure",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden overclaim token: {token}")

print("GRF source audit deepening verification OK.")
