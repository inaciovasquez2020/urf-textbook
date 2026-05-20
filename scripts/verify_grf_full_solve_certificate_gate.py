#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts/grf/full_solve_certificate_gate.json"
DOC = ROOT / "docs/essays/GRF_2026_FULL_SOLVE_CERTIFICATE_GATE.md"

REQUIRED_OBLIGATIONS = {
    "O1_POSITIVE_INNER_BOUNDARY_MARGIN",
    "O2_ACTUAL_DERIVATIVE_DATA",
    "O3_FIRST_CELL_NUMERIC_CERTIFICATE",
    "O4_MULTI_CELL_PROPAGATION",
    "O5_ALL_WEC_DEC_COMPONENTS",
    "O6_MATCHING_THEOREM",
    "O7_PHYSICAL_REALIZATION",
    "O8_FORMAL_VERIFICATION",
}

REQUIRED_DOC_TOKENS = [
    "Status: `FRONTIER_OPEN_FULL_CERTIFICATE_GATE`",
    "\\rho(r_1)-p_t(r_1)\\ge \\eta>0",
    "MISSING_DERIVATIVE_BOUND_CERTIFICATE",
    "\\eta-L_{\\rm cell}\\Delta r\\ge0",
    "MISSING_MULTI_CELL_CERTIFICATE",
    "MISSING_COMPONENT_INVENTORY_CERTIFICATES",
    "MISSING_MATCHING_CERTIFICATE",
    "MISSING_REALIZATION_CERTIFICATE",
    "artifacts/grf/transition\\_shell\\_full\\_certificate\\_input.json",
    "GRF theorem-level closure is forbidden",
    "It does not prove:",
]

REQUIRED_BOUNDARY_TOKENS = [
    "certificate gate only",
    "not a positive inner-boundary margin proof",
    "not derivative data construction",
    "not a first-cell numeric certificate",
    "not a multi-cell interval certificate",
    "not WEC/DEC closure",
    "not a matching theorem",
    "not a physical realization theorem",
    "not GRF theorem-level closure",
]


def main() -> None:
    if not ART.exists():
        raise SystemExit(f"missing artifact: {ART}")
    if not DOC.exists():
        raise SystemExit(f"missing doc: {DOC}")

    artifact = json.loads(ART.read_text(encoding="utf-8"))
    if artifact.get("status") != "FRONTIER_OPEN_FULL_CERTIFICATE_GATE":
        raise SystemExit("gate status must remain FRONTIER_OPEN_FULL_CERTIFICATE_GATE")

    obligations = artifact.get("required_obligations", [])
    found = {item.get("id") for item in obligations}
    missing = REQUIRED_OBLIGATIONS - found
    extra = found - REQUIRED_OBLIGATIONS
    if missing:
        raise SystemExit(f"missing obligations: {sorted(missing)}")
    if extra:
        raise SystemExit(f"unexpected obligations: {sorted(extra)}")

    for item in obligations:
        status = item.get("status", "")
        if not status.startswith("MISSING_"):
            raise SystemExit(f"obligation must remain missing until certified: {item}")

    boundary = "\n".join(artifact.get("boundary", []))
    for token in REQUIRED_BOUNDARY_TOKENS:
        if token not in boundary:
            raise SystemExit(f"missing boundary token: {token}")

    if artifact.get("certificate_input_path") != "artifacts/grf/transition_shell_full_certificate_input.json":
        raise SystemExit("bad certificate input path")

    doc = DOC.read_text(encoding="utf-8")
    for token in REQUIRED_DOC_TOKENS:
        if token not in doc:
            raise SystemExit(f"missing doc token: {token}")

    print("GRF full-solve certificate gate verification OK.")


if __name__ == "__main__":
    main()
