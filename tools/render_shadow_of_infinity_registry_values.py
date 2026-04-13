from __future__ import annotations
import json
from pathlib import Path

DOC = Path("docs/foundations/SHADOW_OF_INFINITY.md")
OUT = Path("artifacts/foundations/shadow_of_infinity_registry_values.json")

TOOLKIT_TOOLS = [
    "Kairos",
    "Newstein Chain",
    "DraG0n",
    "RiGUp",
    "EV0V3",
    "EXNILIO",
    "GQu",
    "FGL",
]

CLAY_PROBLEMS = [
    "P versus NP",
    "Riemann hypothesis",
    "Navier-Stokes existence and smoothness",
    "Yang-Mills existence and mass gap",
    "Hodge conjecture",
    "Birch and Swinnerton-Dyer conjecture",
]

def build_values() -> dict:
    text = DOC.read_text(encoding="utf-8")
    toolkit_presence = {name: (name in text) for name in TOOLKIT_TOOLS}
    clay_presence = {name: (name in text) for name in CLAY_PROBLEMS}
    values = {
        "shadow_formulation_present": r"\mathrm{ShadowOfInfinity}:=\text{a form of the finite close to infinity.}" in text,
        "toolkit_total": len(TOOLKIT_TOOLS),
        "toolkit_present": sum(toolkit_presence.values()),
        "toolkit_missing": len(TOOLKIT_TOOLS) - sum(toolkit_presence.values()),
        "clay_total": len(CLAY_PROBLEMS),
        "clay_present": sum(clay_presence.values()),
        "clay_missing": len(CLAY_PROBLEMS) - sum(clay_presence.values()),
        "toolkit_presence": toolkit_presence,
        "clay_presence": clay_presence,
        "registry_complete": all(toolkit_presence.values()) and all(clay_presence.values()),
    }
    return values

def main() -> int:
    values = build_values()
    OUT.write_text(json.dumps(values, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(values, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
