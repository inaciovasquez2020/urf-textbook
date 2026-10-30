# Claim-Governance Design-Science Case Study: Reproducibility and Open Boundaries

Status: `WORKING_PREPRINT_PACKAGE_NOT_SUBMITTED`

Date recorded: 2026-10-29

## Scope

This note records the state of a research package concerning a proposed lifecycle architecture for verification-governed claim management in large-scale theoretical research programs. It is a research-log entry, not an endorsement, peer review, acceptance notice, or claim of established novelty.

## Reported implementation and data checks

The package report records:

- A formal claim-object schema separating epistemic status, mathematical scope, assumptions, evidence type and verification result, boundaries, frontier obligations, provenance, and promotion history.
- A promotion invariant intended to block `PROVED` status while assumptions or frontier obligations remain active, or matching formal-proof evidence is absent.
- A verifier negative test rejecting an invalid promotion attempt.
- A literature comparison positioning the proposed mechanism as complementary to FEDS, DSVF, and DSR Transparency, not as a replacement for those approaches.
- A recovered supplementary CSV with 24 scoring records: 12 claim objects scored in baseline and governed phases, with 16 indicators per record.
- Reported recomputation: baseline mean 53.50, governed mean 84.17, and 24/24 reported means matching recomputation.
- Original CSV SHA-256: `dc9ebb433c63bd115da6f17062b0fcd8a325037deba93be6ae3e45aa6432562f`.

### Data-protocol correction

The recovered CSV contains indicator values from 0.34 to 1.00. The manuscript's earlier statement that indicators use only `0`, `0.5`, and `1` is inconsistent with the recovered data and must remain corrected to continuous decimal scoring. The inputs must not be silently rounded or replaced by a reconstructed dataset.

The previously reported 10,000-trial sensitivity result remains unverified because its simulation source and execution provenance have not been recovered. It is not evidence for the current result.

## Provisional submission classification

- Provisional primary arXiv category: `cs.SE` (Software Engineering).
- Possible alternative, depending on final framing: `cs.OH` (Other Computer Science).
- No arXiv submission has been made.

The category is an administrative classification choice only. It is not an endorsement, external validation, acceptance, or evidence of novelty.

## Open boundaries

1. **Novelty is not established.** The precise contribution relative to FEDS, DSVF, and DSR Transparency remains to be isolated in a formal novelty-difference matrix. In particular, no unique invariant, state transition, or enforcement capability has yet been established as absent from the prior approaches.
2. **Indicator validity is not independently calibrated.** The arithmetic recomputation verifies reported means against the recovered records; it does not establish that the 16 indicators validly or reliably measure the intended constructs.
3. **Sensitivity analysis is not reproducible yet.** The 10,000-trial simulation source and execution receipt are missing.
4. **Negative-test coverage is incomplete.** Promotion failure conditions require systematic negative tests, not only the reported invalid-promotion example.
5. **Presentation cleanup remains.** LaTeX table-overflow warnings remain to be corrected.

`BOUNDARY :=` Novelty of the proposed lifecycle architecture relative to established design-science frameworks is not established.

`BOUNDARY :=` Independent construct validity and calibration of the 16 scoring indicators are not established.

`BOUNDARY :=` The 10,000-trial sensitivity result is unverified and must not be cited as a reproduced result.

## Next bounded improvement

Construct a claim-by-claim novelty-difference matrix against FEDS, DSVF, and DSR Transparency. For each proposed contribution, identify the exact invariant, state transition, or enforcement capability; cite the corresponding prior-art mechanism; and mark the difference as established, overlapping, or unresolved. Do not claim novelty until each asserted difference has supporting evidence.

## Use and attribution boundary

This is an internal research case-study record of the reported package state as of the date above. It does not assert endorsement by arXiv, a journal, a conference, the authors of the compared frameworks, or any external institution. It does not claim peer review, acceptance, submission, theorem-level proof, independently calibrated measurement validity, or established novelty.
