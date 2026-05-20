#!/usr/bin/env python3
from __future__ import annotations

import json
from numbers import Real
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts/grf/positive_inner_boundary_margin_certificate.json"
DOC = ROOT / "docs/essays/GRF_2026_POSITIVE_INNER_BOUNDARY_MARGIN_CERTIFICATE.md"
INPUT = ROOT / "artifacts/grf/positive_inner_boundary_margin_input.json"

REQUIRED_DOC_TOKENS = [
    "Status: `FRONTIER_OPEN_MARGIN_CERTIFICATE_INTERFACE`",
    "O1:\\qquad \\rho(r_1)-p_t(r_1)\\ge \\eta>0",
    "f(r)=\\rho(r)-p_t(r)",
    "f(r_1)\\ge \\eta>0",
    "f(r_1)-\\eta\\ge0",
    "artifacts/grf/positive\\_inner\\_boundary\\_margin\\_input.json",
    "PositiveInnerBoundaryMargin",
    "It does not prove:",
    "GRF theorem-level closure",
]

REQUIRED_BOUNDARY_TOKENS = [
    "certificate interface only",
    "not a proof that eta exists",
    "not a computation of rho_minus_pt(r1)",
    "not a first-cell positivity certificate",
    "not a multi-cell interval certificate",
    "not WEC/DEC closure",
    "not a matching theorem",
    "not a physical realization theorem",
    "not GRF theorem-level closure",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def validate_optional_input() -> None:
    if not INPUT.exists():
        return

    data = json.loads(INPUT.read_text(encoding="utf-8"))

    require(
        data.get("certificate_id") == "O1_POSITIVE_INNER_BOUNDARY_MARGIN",
        "input certificate_id must be O1_POSITIVE_INNER_BOUNDARY_MARGIN",
    )
    require(data.get("status") == "VERIFIED", "input status must be VERIFIED")

    eta = data.get("eta")
    rho_minus_pt_r1 = data.get("rho_minus_pt_r1")

    require(isinstance(eta, Real), "eta must be numeric")
    require(isinstance(rho_minus_pt_r1, Real), "rho_minus_pt_r1 must be numeric")
    require(eta > 0, "eta must be positive")
    require(rho_minus_pt_r1 >= eta, "rho_minus_pt_r1 must be >= eta")


def main() -> None:
    require(ART.exists(), f"missing artifact: {ART}")
    require(DOC.exists(), f"missing doc: {DOC}")

    artifact = json.loads(ART.read_text(encoding="utf-8"))

    require(
        artifact.get("id") == "GRF_2026_POSITIVE_INNER_BOUNDARY_MARGIN_CERTIFICATE",
        "bad artifact id",
    )
    require(
        artifact.get("status") == "FRONTIER_OPEN_MARGIN_CERTIFICATE_INTERFACE",
        "artifact must remain an open certificate interface",
    )
    require(
        artifact.get("obligation") == "O1_POSITIVE_INNER_BOUNDARY_MARGIN",
        "bad obligation id",
    )
    require(
        artifact.get("required_object") == "rho_minus_pt(r1) >= eta > 0",
        "bad required object",
    )
    require(
        artifact.get("certificate_input_path")
        == "artifacts/grf/positive_inner_boundary_margin_input.json",
        "bad certificate input path",
    )

    boundary = "\n".join(artifact.get("boundary", []))
    for token in REQUIRED_BOUNDARY_TOKENS:
        require(token in boundary, f"missing boundary token: {token}")

    doc = DOC.read_text(encoding="utf-8")
    for token in REQUIRED_DOC_TOKENS:
        require(token in doc, f"missing doc token: {token}")

    validate_optional_input()

    print("GRF positive inner-boundary margin certificate interface verification OK.")


if __name__ == "__main__":
    main()
