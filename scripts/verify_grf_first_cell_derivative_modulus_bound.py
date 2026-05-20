#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/essays/GRF_2026_FIRST_CELL_DERIVATIVE_MODULUS_BOUND.md"
ART = ROOT / "artifacts/grf/first_cell_derivative_modulus_bound.json"

REQUIRED_DOC_TOKENS = [
    "Status: `CONDITIONAL_DERIVATIVE_MODULUS_BOUND`",
    "FirstCellDerivativeModulusBound",
    "L_{\\rm cell}",
    "A(r)=1-\\frac{2m(r)}{r}",
    "B(r)=\\frac{r m'(r)-m(r)}{r^2 A(r)}",
    "Q'",
    "\\Phi'''",
    "\\eta-L_{\\rm cell}\\Delta r\\ge0",
    "It does not prove:",
    "GRF theorem-level closure",
]

REQUIRED_ARTIFACT_FIELDS = {
    "id": "GRF_2026_FIRST_CELL_DERIVATIVE_MODULUS_BOUND",
    "status": "CONDITIONAL_DERIVATIVE_MODULUS_BOUND",
    "minimal_missing_assumption_closed": "FirstCellDerivativeData(r0,a,M0,M1,M2,P1,P2,P3)",
}


def main() -> None:
    if not DOC.exists():
        raise SystemExit(f"missing doc: {DOC}")
    if not ART.exists():
        raise SystemExit(f"missing artifact: {ART}")

    doc = DOC.read_text(encoding="utf-8")
    for token in REQUIRED_DOC_TOKENS:
        if token not in doc:
            raise SystemExit(f"missing doc token: {token}")

    artifact = json.loads(ART.read_text(encoding="utf-8"))
    for key, expected in REQUIRED_ARTIFACT_FIELDS.items():
        actual = artifact.get(key)
        if actual != expected:
            raise SystemExit(f"bad artifact field {key}: expected {expected!r}, got {actual!r}")

    boundary = "\n".join(artifact.get("boundary", []))
    for token in [
        "conditional derivative modulus only",
        "not a proof that the derivative data exist",
        "not WEC/DEC closure",
        "not GRF theorem-level closure",
    ]:
        if token not in boundary:
            raise SystemExit(f"missing boundary token: {token}")

    print("GRF first-cell derivative modulus bound verification OK.")


if __name__ == "__main__":
    main()
