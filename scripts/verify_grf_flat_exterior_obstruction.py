#!/usr/bin/env python3
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_FLAT_EXTERIOR_OBSTRUCTION.md")
text = DOC.read_text(encoding="utf-8")

required = [
    "Flat-Exterior Obstruction",
    "Conditional structural obstruction.",
    "m(r)=\\frac r2\\left(1-e^{-2\\Lambda(r)}\\right)",
    "m'(r)=4\\pi r^2\\rho(r)",
    "\\rho\\ge0",
    "m_{\\mathrm{loc}}(r)>0",
    "A flat exterior has",
    "m_{\\mathrm{flat}}(r)=0",
    "a WEC-preserving transition from the local alpha-beta certificate to a flat exterior cannot exist",
    "positive-mass Schwarzschild exterior",
    "M\\ge m_{\\mathrm{loc}}(r_1)",
    "It does not construct the Schwarzschild matching shell.",
    "A computable positive-mass Schwarzschild transition-shell certificate",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

forbidden = [
    "global existence is proved",
    "semiclassical stability is proved",
    "schwarzschild matching shell is constructed",
    "unconditional gravitational closure",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden token: {token}")

print("GRF flat-exterior obstruction verification OK.")
