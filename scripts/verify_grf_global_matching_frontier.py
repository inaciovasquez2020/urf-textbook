#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/essays/GRF_2026_GLOBAL_MATCHING_FRONTIER.md")
text = path.read_text(encoding="utf-8")

required = [
    "Global Matching Frontier",
    "Frontier note.",
    "It does not claim a global Einstein-matter construction theorem.",
    "\\alpha(r)=e^{-2ar}",
    "\\beta(r)=e^{2ar}",
    "Energy-condition functionals",
    "Smooth junction condition",
    "Global Matching Lemma",
    "This document does not prove the Global Matching Lemma.",
    "Weakest constructive route",
    "A computable transition-shell certificate",
    "\\rho\\ge0",
    "\\rho+p_r\\ge0",
    "\\rho+p_t\\ge0",
    "\\rho-p_r\\ge0",
    "\\rho-p_t\\ge0",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

forbidden = [
    "global matching lemma is proved",
    "global einstein-matter construction theorem is proved",
    "asymptotic flatness is proved",
    "semiclassical stability is proved",
    "unconditional gravitational closure",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden overclaim token: {token}")

print("GRF global matching frontier verification OK.")
