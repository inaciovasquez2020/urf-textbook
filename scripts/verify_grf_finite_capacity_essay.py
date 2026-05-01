#!/usr/bin/env python3
from pathlib import Path
import re
import sys

path = Path("docs/essays/GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex")
text = path.read_text(encoding="utf-8")

required = [
    "Finite-capacity geometry",
    "Finite-capacity outward deflection",
    "Outward deflection is admissible only when",
    "infinite operational gain",
    "does not rely on external manuscripts",
    "No singularity or exotic source is required by the sign condition alone",
]

for token in required:
    if token not in text:
        raise SystemExit(f"missing required token: {token}")

forbidden = [
    "proves quantum gravity",
    "solves quantum gravity",
    "proves general relativity is incomplete",
    "disproves energy conditions",
    "unconditional proof of repulsive gravity",
    "negative mass is real",
]

lower = text.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden overclaim token: {token}")

if "\\begin{lemma}[Finite-capacity outward deflection]" not in text:
    raise SystemExit("missing named finite-capacity lemma")

if "\\begin{proof}" not in text or "\\end{proof}" not in text:
    raise SystemExit("missing proof environment")

ineq_patterns = [
    r"\\sup_\{\\Omega\}",
    r"C_\{\\mathrm\{cap\}\}",
    r"\\partial_r n\(r\)>0",
    r"\\partial_r \\alpha\(r\)<0",
]
for pattern in ineq_patterns:
    if not re.search(pattern, text):
        raise SystemExit(f"missing expected mathematical anchor: {pattern}")

print("GRF finite-capacity essay verification OK.")
