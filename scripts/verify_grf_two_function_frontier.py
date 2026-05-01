#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/essays/GRF_2026_FINITE_CAPACITY_TWO_FUNCTION_FRONTIER.md")
text = path.read_text(encoding="utf-8")

required = [
    "Two-Function Frontier",
    "ds^2=-\\alpha(r)dt^2+\\beta(r)dr^2+r^2d\\Omega^2",
    "G^t_t",
    "G^r_r",
    "G^\\theta_\\theta",
    "8\\pi\\rho",
    "8\\pi p_r",
    "8\\pi p_t",
    "\\Phi'(r)<0",
    "\\rho+p_r\\ge0",
    "\\frac{\\beta'}{\\beta}\n+\n2\\Phi'\n\\ge0",
    "\\frac{\\beta'}{\\beta}\n\\ge\n-2\\Phi'.",
    "Two-Function Finite-Capacity Realization Lemma",
    "The next missing object is an explicit bounded pair",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

forbidden = [
    "solves gravity",
    "proves repulsive gravity",
    "unconditional gravitational realization",
    "all energy conditions are satisfied",
    "quantum gravity is solved",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden overclaim token: {token}")

print("GRF two-function frontier verification OK.")
