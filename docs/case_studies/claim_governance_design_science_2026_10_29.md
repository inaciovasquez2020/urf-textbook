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


## Preliminary novelty-difference matrix (2026-10-30)

### Comparison basis and limitation

This is a bounded, abstract-and-framework-level comparison against the identified primary publications. It is not a systematic literature review, and it does not establish that a capability is absent from an entire framework merely because it is not stated in the abstract or summary inspected. The manuscript's complete architecture, schema, transition rules, and implementation must be mapped against full texts and adjacent work before any novelty claim is made.

| Proposed URF capability or claim | FEDS | DSVF | DSR Transparency | MEDS (2026) | Preliminary difference assessment |
|---|---|---|---|---|---|
| Plan artifact evaluation across purpose, timing, method, and properties | Direct overlap: FEDS guides why, when, how, and what to evaluate; distinguishes formative/summative and artificial/naturalistic evaluation and supplies a four-step design process. | Related but different emphasis: validity types and evidence appropriate to claims, rather than an evaluation-strategy taxonomy. | Evaluation transparency is one of six transparency dimensions. | Directly adjacent: MEDS is a methodology for evaluating design-science artifacts and addresses evaluation burden and rigor. | Not a novelty basis. URF must not claim to originate evaluation planning or evaluation lifecycle guidance. |
| Classify claims and connect them to validity/evidence | FEDS connects evaluation goals and artifact properties to evaluation episodes. | Strong overlap: DSVF explicitly structures criterion, causal, and context claims and their validity subtypes, with a claim–evaluation–evidence argument. | Supports transparent reporting of assumptions, scope, data, results, analyses, and implications, including contribution transparency. | Evaluation methodology is adjacent; exact overlap with URF claim-object semantics requires full-text comparison. | Strong conceptual overlap. A claim schema alone is not established as novel. URF must show a materially different formal semantics or enforceable operation, not merely different field names. |
| Record process, problem, solution, build, evaluation, and contribution transparently | FEDS covers evaluation design and episodes, not the entire transparency taxonomy in its stated scope. | DSVF addresses validity of artifact knowledge claims, not the same six-part transparency taxonomy. | Direct overlap: these are the six stated transparency forms. | Related to evaluation practice; full-text mapping required. | Not a novelty basis for provenance or transparent reporting in general. |
| Represent epistemic status, assumptions, scope, boundaries, evidence, and open obligations in a machine-readable claim object | FEDS gives evaluation strategy guidance; the inspected description does not establish a corresponding machine-readable claim-object schema. | DSVF provides claim/validity categories and evidence argumentation; the inspected description does not establish URF's exact data model or promotion rule. | DSR Transparency provides reporting dimensions; the inspected description does not establish URF's exact machine-readable state model. | Full-text comparison required; no absence claim is made. | Candidate architectural distinction only. The actual schema and its semantics must be compared with prior claim, provenance, assurance-case, and research-object models. |
| Enforce a promotion invariant that blocks `PROVED` while assumptions or frontier obligations remain active or matching formal-proof evidence is absent | No equivalent invariant is established by the FEDS summary reviewed; FEDS is principally an evaluation strategy framework. | DSVF's validity/evidence structure is closely related conceptually, but the reviewed source does not establish this exact automated status gate. | Transparency guidance is not, on the reviewed description, an executable promotion policy. | Full text not yet checked for analogous gates or lifecycle rules. | Strongest candidate for a technical difference, but currently **unresolved**. Need exact formal rule, executable verifier semantics, failure cases, and prior-art search. Absence from summaries is not proof of novelty. |
| Preserve provenance and promotion history as machine-checkable lifecycle state | FEDS includes iterative evaluation trajectories; whether it specifies equivalent event-level provenance and immutable promotion history is not established by the source summary. | DSVF requires evidence argumentation; exact event provenance and transition history are not established by the inspected description. | Process and build transparency overlap with documenting lifecycle history; machine-enforced event semantics are not established by the inspected description. | Full-text comparison required. | Partial overlap is clear; machine-enforced provenance/history may be a candidate implementation distinction, not yet a demonstrated novel contribution. |
| Systematically reject invalid status transitions and test each failure condition | FEDS supports rigorous evaluation design but is not described as a transition validator. | DSVF supports validity reasoning but is not described in the inspected source as an executable state-transition verifier. | Transparency guidance promotes disclosure; the inspected description does not specify executable transition rejection. | Full-text comparison required. | Candidate software-engineering contribution. Must demonstrate exhaustive transition rules, adversarial/negative tests, and distinction from established workflow engines, assurance cases, policy-as-code, and proof-carrying systems. |
| Empirically demonstrate improved claim-governance outcomes using 12 claim objects and 16 indicators | FEDS is relevant to evaluation design and would inform how this artifact should be evaluated. | DSVF directly challenges validity of the outcome claims and the measurement/evidence chain. | Evaluation and contribution transparency require reporting the design and evidence. | MEDS is directly relevant to choosing and justifying an evaluation methodology. | Not established. Arithmetic agreement verifies calculations only; it does not calibrate indicators, establish causal effects, or validate the construct. |

### Matrix conclusion

The literature comparison does not presently establish a novel lifecycle architecture. FEDS, DSVF, DSR Transparency, and MEDS cover substantial neighboring territory in evaluation planning, claim validity, evidence argumentation, lifecycle transparency, and artifact evaluation. The most plausible candidate distinction is the proposed executable promotion gate over a machine-readable claim state, potentially combined with provenance and transition-history enforcement. That candidate remains unresolved until its formal semantics and implementation are compared against the wider literature and existing technical systems.

The matrix must be read conservatively:
- **Established overlap** means the cited framework explicitly covers the neighboring function.
- **Candidate difference** means only that the currently inspected descriptions do not establish the same specific mechanism; it does not mean the mechanism is absent from the literature.
- **Unresolved** means the evidence is insufficient to decide.

### Primary literature examined

1. Venable, J., Pries-Heje, J., & Baskerville, R. (2016). [FEDS: A Framework for Evaluation in Design Science Research](https://doi.org/10.1057/ejis.2014.36). *European Journal of Information Systems*, 25, 77–89.
2. Larsen, K. R., Lukyanenko, R., Mueller, R. M., Storey, V. C., Parsons, J., VanderMeer, D., & Hovorka, D. (2025). [Validity in Design Science](https://aisel.aisnet.org/misq/vol49/iss4/7/). *MIS Quarterly*, 49(4), 1267–1294.
3. [Transparency in design science research](https://doi.org/10.1016/j.dss.2024.114236). *Decision Support Systems*, 182 (2024), 114236.
4. Baskerville, R., Pries-Heje, J., & Venable, J. R. (2026). [MEDS: Methodology for Evaluation in Design Science](https://doi.org/10.1080/0960085X.2026.2627280). *European Journal of Information Systems*, 35(5), 830–847. Published online 12 February 2026.

## Updated bounded next action

Formalize the promotion gate as a transition relation over the actual claim-object schema. For each transition, state preconditions, required evidence type, prohibited states, and verifier behavior; then compare that exact relation against full texts and adjacent work on assurance cases, proof-carrying claims, workflow/policy engines, provenance systems, and research-object lifecycle management. Until that comparison is complete, retain:

`BOUNDARY :=` Novelty of the proposed lifecycle architecture is not established.
