#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts/urf11/clr_deep_line_audit_2026_05_25.json"
DOC = ROOT / "docs/status/URF11_CLR_DEEP_LINE_AUDIT_2026_05_25.md"

REQUIRED_BOUNDARY = [
    "audit_only",
    "does_not_rewrite_files",
    "does_not_prove_unguarded_cycle_local_rigidity",
    "does_not_prove_high_COR_forces_full_FOk_type_diversity",
    "does_not_prove_Chronos_RR",
    "does_not_prove_H4_1_FGL",
    "does_not_prove_P_vs_NP",
    "does_not_prove_any_Clay_problem",
]

def main():
    data = json.loads(ART.read_text())
    doc = DOC.read_text()

    assert data["artifact"] == "clr_deep_line_audit_2026_05_25"
    assert data["scope"] == "all git-tracked UTF-8 text files in urf-textbook"
    assert data["status"] in {
        "CLR_DEEP_LINE_AUDIT_REVIEW_REQUIRED",
        "CLR_DEEP_LINE_AUDIT_NO_UNSAFE_REMAINDERS_DETECTED",
    }
    assert isinstance(data["findings"], list)
    assert data["total_findings"] == len(data["findings"])
    assert data["review_required_count"] == sum(1 for f in data["findings"] if f["requires_review"])
    assert data["danger_findings_count"] == sum(
        1 for f in data["findings"]
        if f["danger_token_present"] and not (f["safe_by_file"] or f["safe_by_token"])
    )

    for token in REQUIRED_BOUNDARY:
        assert token in data["boundary"], token

    for token in [
        "URF-11 CLR Deep Line Audit",
        "Does not prove unguarded cycle-local rigidity",
        "Does not prove high COR forcing full FO^k type diversity",
        "Does not prove Chronos-RR",
        "Does not prove H4.1/FGL",
        "Does not prove P vs NP",
        "Does not prove any Clay problem",
    ]:
        assert token in doc, token

    print("OK: URF-11 CLR deep line audit verified")

if __name__ == "__main__":
    main()
