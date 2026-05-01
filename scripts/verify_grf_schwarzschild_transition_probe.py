#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

DOC = Path("docs/essays/GRF_2026_SCHWARZSCHILD_TRANSITION_PROBE.md")
TOOL = Path("tools/grf_schwarzschild_transition_probe.py")
ARTIFACT = Path("artifacts/grf/schwarzschild_transition_probe.json")

for path in [DOC, TOOL]:
    if not path.exists():
        raise SystemExit(f"missing required file: {path}")

doc = DOC.read_text(encoding="utf-8")
required = [
    "Computable frontier probe.",
    "It does not claim a global matching theorem.",
    "positive-mass Schwarzschild",
    "M\\ge m_{\\mathrm{loc}}(r_1)",
    "This is not interval arithmetic.",
    "A sampled pass is not a theorem.",
    "A sampled failure is not an impossibility theorem.",
    "interval-certified positive-mass Schwarzschild transition ansatz",
]

for token in required:
    if token not in doc:
        raise SystemExit(f"missing required doc token: {token}")

forbidden = [
    "global matching theorem is proved",
    "interval arithmetic certificate is proved",
    "impossibility theorem is proved",
    "unconditional gravitational closure",
]

lower = doc.lower()
for token in forbidden:
    if token in lower:
        raise SystemExit(f"forbidden doc token: {token}")

subprocess.run(["python3", str(TOOL)], check=True)

payload = json.loads(ARTIFACT.read_text(encoding="utf-8"))
if payload.get("status") not in {"PASS_NUMERICAL_SAMPLE", "FRONTIER_FAIL"}:
    raise SystemExit(f"unexpected status: {payload.get('status')}")

if payload.get("candidate_count", 0) <= 0:
    raise SystemExit("candidate_count must be positive")

best = payload.get("best_candidate", {})
if "min_margins" not in best:
    raise SystemExit("best candidate missing min_margins")

if payload.get("next_missing_object") != "interval-certified positive-mass Schwarzschild transition ansatz":
    raise SystemExit("wrong next missing object")

print("GRF Schwarzschild transition probe verification OK.")
