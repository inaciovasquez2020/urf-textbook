#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT.md")
text = path.read_text(encoding="utf-8")

required = [
    "Source Audit",
    "Optical metrics are legitimate effective-geometric objects",
    "Analogue gravity is an established research program",
    "Transformation optics supports geometry-of-light engineering",
    "Graded-index optics provides bounded refractive-index examples",
    "Energy conditions are admissibility filters",
    "Quantum focusing supports the modern information/geometry direction",
    "Two-function metric freedom is the correct realization frontier",
    "Explicit bounded realization pair",
    "It is not yet a full gravitational realization theorem",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

urls = [
    "gordon_-_optical_metrics.pdf",
    "10.12942/lrr-2011-3",
    "0805.4778",
    "ao-17-24-3990",
    "2003.01815",
    "10.1103/PhysRevD.93.064044",
    "0712.0713",
]

for token in urls:
    if token not in text:
        raise SystemExit(f"missing source URL/token: {token}")

forbidden = [
    "proves finite capacity",
    "proves repulsive gravity",
    "solves semiclassical gravity",
    "full gravitational realization theorem is proved",
    "all energy conditions are satisfied",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden overclaim token: {token}")

print("GRF source audit verification OK.")
