#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/essays/GRF_2026_EXPLICIT_ALPHA_BETA_PAIR.md")
text = path.read_text(encoding="utf-8")

required = [
    "Explicit Local Alpha-Beta Pair",
    "Conditional local realization certificate",
    "\\alpha(r)=e^{-2ar}",
    "\\beta(r)=e^{2ar}",
    "\\Phi'(r)=-a<0",
    "\\partial_r n(r)=ae^{ar}>0",
    "p_r=-\\rho",
    "\\rho+p_r=0",
    "\\frac{\\beta'}{\\beta}+2\\Phi'=0",
    "the weak energy condition holds",
    "the dominant energy condition holds",
    "This is a local annular certificate.",
    "The next missing object is a global matching lemma",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

forbidden = [
    "global theorem",
    "asymptotic flatness is proved",
    "quantum stability is proved",
    "physical material realization is proved",
    "solves gravity",
    "unconditional gravitational closure",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden overclaim token: {token}")

print("GRF explicit alpha-beta pair verification OK.")
