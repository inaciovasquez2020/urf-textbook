#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "complete": ROOT / "artifacts/grf/complete_transition_shell_certificate_schema.json",
    "o2": ROOT / "artifacts/grf/o2_derivative_data_certificate_interface.json",
    "multi": ROOT / "artifacts/grf/multi_cell_interval_certificate_interface.json",
    "wec_dec": ROOT / "artifacts/grf/wec_dec_component_inventory_gate.json",
    "matching": ROOT / "artifacts/grf/matching_realization_theorem_gate.json",
    "doc": ROOT / "docs/essays/GRF_2026_TRANSITION_SHELL_CERTIFICATE_SCHEMA_PACK.md",
}

REQUIRED_STATUSES = {
    "complete": "FRONTIER_OPEN_SCHEMA_ONLY",
    "o2": "FRONTIER_OPEN_DERIVATIVE_DATA_INTERFACE",
    "multi": "FRONTIER_OPEN_MULTI_CELL_INTERFACE",
    "wec_dec": "FRONTIER_OPEN_COMPONENT_GATE",
    "matching": "FRONTIER_OPEN_MATCHING_REALIZATION_GATE",
}

REQUIRED_GATES = {
    "O1_POSITIVE_INNER_BOUNDARY_MARGIN",
    "O2_ACTUAL_DERIVATIVE_DATA",
    "O3_FIRST_CELL_NUMERIC_CERTIFICATE",
    "O4_MULTI_CELL_INTERVAL_PROPAGATION",
    "O5_WEC_DEC_COMPONENT_INVENTORY",
    "O6_MATCHING_THEOREM",
    "O7_PHYSICAL_REALIZATION_THEOREM",
    "O8_FINAL_EXECUTABLE_VERIFICATION",
}

REQUIRED_DOC_TOKENS = [
    "Status: `FRONTIER_OPEN_SCHEMA_PACK`",
    "CompleteGRFTransitionShellCertificate",
    "O2_ACTUAL_DERIVATIVE_DATA",
    "O4_MULTI_CELL_INTERVAL_PROPAGATION",
    "O5_WEC_DEC_COMPONENT_INVENTORY",
    "O6_MATCHING_THEOREM",
    "O7_PHYSICAL_REALIZATION_THEOREM",
    "GRF theorem-level closure is forbidden",
    "It does not prove:",
    "GRF theorem-level closure",
]

REQUIRED_BOUNDARY_TOKENS = [
    "not WEC/DEC closure",
    "not a matching theorem",
    "not a physical realization theorem",
    "not GRF theorem-level closure",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def load_json(name: str) -> dict:
    path = FILES[name]
    require(path.exists(), f"missing file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in FILES.values():
        require(path.exists(), f"missing file: {path}")

    complete = load_json("complete")
    require(
        complete.get("schema_name") == "CompleteGRFTransitionShellCertificate",
        "missing complete schema name",
    )
    require(set(complete.get("required_gates", [])) == REQUIRED_GATES, "bad required gate set")

    for name, status in REQUIRED_STATUSES.items():
        data = load_json(name)
        require(data.get("status") == status, f"bad status for {name}")
        boundary = "\n".join(data.get("boundary", []))
        for token in REQUIRED_BOUNDARY_TOKENS:
            require(token in boundary, f"missing boundary token in {name}: {token}")

    o2 = load_json("o2")
    for field in ["r0", "a", "M0", "M1", "M2", "P1", "P2", "P3", "L_cell"]:
        require(field in o2.get("required_fields", []), f"missing O2 required field: {field}")

    multi = load_json("multi")
    require("cell.eta" in multi.get("required_fields", []), "missing multi-cell eta field")
    require("cell.L" in multi.get("required_fields", []), "missing multi-cell L field")

    wec_dec = load_json("wec_dec")
    for component in ["rho >= 0", "rho + p_r >= 0", "rho + p_t >= 0", "rho - |p_r| >= 0", "rho - |p_t| >= 0", "rho - p_t >= 0"]:
        require(component in wec_dec.get("required_components", []), f"missing WEC/DEC component: {component}")

    matching = load_json("matching")
    require("O6_MATCHING_THEOREM" in matching.get("obligations", []), "missing O6")
    require("O7_PHYSICAL_REALIZATION_THEOREM" in matching.get("obligations", []), "missing O7")

    doc = FILES["doc"].read_text(encoding="utf-8")
    for token in REQUIRED_DOC_TOKENS:
        require(token in doc, f"missing doc token: {token}")

    print("GRF transition-shell certificate schema pack verification OK.")


if __name__ == "__main__":
    main()
