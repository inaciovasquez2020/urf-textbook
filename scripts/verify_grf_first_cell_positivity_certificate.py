#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/essays/GRF_2026_FIRST_CELL_POSITIVITY_CERTIFICATE.md"
ART = ROOT / "artifacts/grf/first_cell_positivity_certificate.json"

REQUIRED_DOC_TOKENS = [
    "Status: `CONDITIONAL_FIRST_CELL_CERTIFICATE`",
    "f(r)=\\rho-p_t",
    "I=[r_1,r_1+\\Delta r]",
    "f(r_1)\\ge \\eta",
    "|f'(r)|\\le L_{\\rm cell}",
    "\\eta-L_{\\rm cell}\\Delta r\\ge0",
    "\\rho(r)-p_t(r)\\ge0",
    "mean-value estimate",
    "It does not prove:",
    "GRF theorem-level closure",
]

REQUIRED_ARTIFACT_FIELDS = {
    "id": "GRF_2026_FIRST_CELL_POSITIVITY_CERTIFICATE",
    "status": "CONDITIONAL_FIRST_CELL_CERTIFICATE",
    "minimal_missing_assumption_closed": "FirstCellCertificateData(eta,dr,L_cell)",
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

    required_inputs = {
        "GRF_2026_INNER_BOUNDARY_SIGN_CONDITION",
        "GRF_2026_RHO_MINUS_PT_BOUNDARY_LEMMA",
        "GRF_2026_FIRST_CELL_INTERVAL_EXTENSION_LEMMA",
        "GRF_2026_FIRST_CELL_DERIVATIVE_MODULUS_BOUND",
    }
    inputs = set(artifact.get("inputs", []))
    missing = required_inputs - inputs
    if missing:
        raise SystemExit(f"missing artifact inputs: {sorted(missing)}")

    boundary = "\n".join(artifact.get("boundary", []))
    for token in [
        "conditional first-cell certificate only",
        "not a proof that eta is positive",
        "not a proof that L_cell derivative data exist",
        "not WEC/DEC closure",
        "not GRF theorem-level closure",
    ]:
        if token not in boundary:
            raise SystemExit(f"missing boundary token: {token}")

    print("GRF first-cell positivity certificate verification OK.")


if __name__ == "__main__":
    main()
