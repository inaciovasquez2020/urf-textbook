#!/usr/bin/env python3
"""
VTD real-packet readiness gate.

This gate verifies that the VTD_MECHANISM_PACKET input surface has been
replaced by real packet content before a mechanism-level verifier run is
treated as admissible.

Boundary:
    This tool does not certify a trajectory anomaly.
    This tool does not prove an anti-gravity mechanism.
    This tool does not identify a physical anti-gravity mechanism.
    This tool is not a theorem-level URF closure claim.
"""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path("VTD_MECHANISM_PACKET")

REQUIRED_FILES = [
    "mechanism_off_real_001.csv",
    "mechanism_on_real_001.csv",
    "control_schedule_u_real.csv",
    "g_certificate_real.yml",
    "eps_meas_certificate_real.yml",
    "eps_F_budget_real.csv",
    "protocol_on_off_real.md",
]

REQUIRED_DIRS = [
    "calibration_records",
    "environment_logs",
    "blinded_replication",
]


def fail(msgs: list[str]) -> int:
    print("vtd_packet_readiness = NOT_READY")
    for msg in msgs:
        print(f"missing_or_stub = {msg}")
    print("claim_boundary = real empirical packet not yet admissible")
    return 1


def main() -> int:
    errors: list[str] = []

    if not ROOT.exists():
        return fail(["VTD_MECHANISM_PACKET directory missing"])

    for name in REQUIRED_FILES:
        path = ROOT / name
        if not path.exists():
            errors.append(f"{name} missing")
            continue
        text = path.read_text(errors="replace")
        if "STUB_ONLY" in text:
            errors.append(f"{name} still contains STUB_ONLY")
        if "contains no real empirical VTD" in text:
            errors.append(f"{name} declares no real empirical VTD data")

    for name in REQUIRED_DIRS:
        path = ROOT / name
        if not path.is_dir():
            errors.append(f"{name}/ missing")
        elif not any(p.name != ".gitkeep" for p in path.iterdir()):
            errors.append(f"{name}/ contains no real records")

    g_cert = ROOT / "g_certificate_real.yml"
    if g_cert.exists():
        text = g_cert.read_text(errors="replace")
        for key in ["station_or_site", "gravity_mgal", "g_cert_m_s2", "eps_g_m_s2"]:
            if f"{key}: null" in text:
                errors.append(f"g_certificate_real.yml has null {key}")

    eps_meas = ROOT / "eps_meas_certificate_real.yml"
    if eps_meas.exists():
        text = eps_meas.read_text(errors="replace")
        if "eps_meas_m_s2: null" in text:
            errors.append("eps_meas_certificate_real.yml has null eps_meas_m_s2")
        if "contains_real_empirical_data: false" in text:
            errors.append("eps_meas_certificate_real.yml declares contains_real_empirical_data false")

    eps_f = ROOT / "eps_F_budget_real.csv"
    if eps_f.exists():
        text = eps_f.read_text(errors="replace")
        if ",null," in text or ",null\n" in text:
            errors.append("eps_F_budget_real.csv contains null force-budget entries")

    if errors:
        return fail(errors)

    print("vtd_packet_readiness = READY")
    print("claim_boundary = packet readiness only; physical anti-gravity mechanism not identified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
