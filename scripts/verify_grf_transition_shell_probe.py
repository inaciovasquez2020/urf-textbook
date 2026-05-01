#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_TRANSITION_SHELL_PROBE.md")
TOOL = Path("tools/grf_transition_shell_probe.py")
ARTIFACT = Path("artifacts/grf/transition_shell_probe.json")

for path in [DOC, TOOL]:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
required = [
    "Computable frontier probe.",
    "It does not claim a global matching theorem.",
    "The default smoothstep-to-flat transition is expected to fail",
    "This is not interval arithmetic.",
    "It is not an impossibility theorem.",
    "It is not a global-existence theorem.",
    "A transition ansatz with interval-certified nonnegative margins",
]

for token in required:
    if token not in doc:
        raise SystemExit(f"missing required doc token: {token}")

forbidden = [
    "global matching theorem is proved",
    "impossibility theorem is proved",
    "global-existence theorem is proved",
    "unconditional gravitational closure",
]

lower = doc.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden doc token: {token}")

subprocess.run(["python3", str(TOOL)], check=True)

payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
if payload.get("status") != "FRONTIER_FAIL":
    raise SystemExit(f"expected FRONTIER_FAIL, got {payload.get('status')}")

margins = payload.get("min_margins", {})
if not margins:
    raise SystemExit("missing min_margins")

if not any(item["value"] < 0 for item in margins.values()):
    raise SystemExit("expected at least one negative sampled margin")

if "smoothstep" not in payload.get("candidate", ""):
    raise SystemExit("missing smoothstep candidate label")

print("GRF transition-shell probe verification OK.")
