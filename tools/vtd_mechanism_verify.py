#!/usr/bin/env python3
"""
VTD ON/OFF mechanism-packet verifier.

Boundary:
    This verifier checks whether an OFF trajectory fails to reject H0 while an
    ON trajectory rejects H0 under the same supplied bounds.

    It does not prove an anti-gravity mechanism.
    It does not identify a physical anti-gravity mechanism.
    It is not a theorem-level URF closure claim.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VTD_VERIFY = ROOT / "tools" / "vtd_verify.py"


def run_vtd(csv: Path, args: argparse.Namespace) -> str:
    cmd = [
        sys.executable,
        str(VTD_VERIFY),
        str(csv),
        "--m",
        str(args.m),
        "--g",
        str(args.g),
        "--eps-meas",
        str(args.eps_meas),
        "--eps-F",
        str(args.eps_F),
        "--eps-g",
        str(args.eps_g),
        "--window",
        str(args.window),
        "--degree",
        str(args.degree),
        "--quiet",
    ]
    proc = subprocess.run(cmd, check=False, text=True, capture_output=True)
    if proc.returncode != 0:
        raise SystemExit(proc.stderr or proc.stdout)
    return proc.stdout


def decision(output: str) -> str:
    for line in output.splitlines():
        if line.startswith("decision = "):
            return line.split("=", 1)[1].strip()
    raise SystemExit("missing decision line from vtd verifier")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser()
    ap.add_argument("--off", required=True, type=Path)
    ap.add_argument("--on", required=True, type=Path)
    ap.add_argument("--control", required=True, type=Path)
    ap.add_argument("--m", required=True, type=float)
    ap.add_argument("--g", required=True, type=float)
    ap.add_argument("--eps-meas", required=True, type=float)
    ap.add_argument("--eps-F", required=True, type=float)
    ap.add_argument("--eps-g", default=0.0, type=float)
    ap.add_argument("--window", default=31, type=int)
    ap.add_argument("--degree", default=4, type=int)
    return ap.parse_args()


def main() -> int:
    args = parse_args()

    for name in ("off", "on", "control"):
        path = getattr(args, name)
        if not path.exists():
            raise SystemExit(f"missing required file: {path}")

    off_out = run_vtd(args.off, args)
    on_out = run_vtd(args.on, args)

    off_decision = decision(off_out)
    on_decision = decision(on_out)

    print(f"off_decision = {off_decision}")
    print(f"on_decision = {on_decision}")

    if off_decision == "H0_NOT_REJECTED" and on_decision == "H0_REJECTED":
        print("mechanism_packet_decision = ON_OFF_ANOMALY_PATTERN_CERTIFIED")
        print("claim_boundary = mechanism-level evidence pattern only; physical anti-gravity mechanism not identified")
        return 0

    print("mechanism_packet_decision = ON_OFF_ANOMALY_PATTERN_NOT_CERTIFIED")
    print("claim_boundary = failure to certify ON/OFF mechanism pattern; physical anti-gravity mechanism not identified")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
