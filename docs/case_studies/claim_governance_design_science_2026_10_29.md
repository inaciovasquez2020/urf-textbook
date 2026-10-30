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


## Promotion-gate formalization and adjacent-system comparison (2026-10-30)

### Evidence boundary and implementation provenance

The case-study package description above reports a richer claim object with epistemic status, mathematical scope, assumptions, evidence, boundaries, frontier obligations, provenance, and promotion history. The current textbook repository note does not contain that package's complete schema or verifier source. Therefore, the formalization below distinguishes (A) behavior directly verified in the related URF Core verifier from (B) the stronger intended transition semantics that remain a specification target. The two must not be conflated.

A related implementation was inspected in `inaciovasquez2020/urf-core`:

- `tools/verify_zero_overclaim.py`, blob `758f87e8d8ed057feb72c44a85eefa017a334233`.
- `tests/test_zero_overclaim.py`, blob `e8fb807859f529b39edb6125af159a6a907d3b0d`.
- `artifacts/status/claim_registry.json`, blob `f40de941d1c9d2ba5f999ccf54fb64da6246070c`.

The verifier's allowed status set is:
`S = {PROVED, RESTRICTED, CONDITIONAL, INTERFACE_ONLY, OPEN, NOT_CLAIMED}`.

For a claim record (c), the observed snapshot-admission predicate for `PROVED` is:

[
\operatorname{AdmitProved}(c) \iff
(c.status = PROVED)
\land (c.unresolved\_obligations = \varnothing)
\land (c.evidence \ne \varnothing)
\land \operatorname{ReceiptOK}(c)
\land \operatorname{RevisionMatch}(c),
]

where:

[
\operatorname{ReceiptOK}(c) \iff
c.verification \text{ is an object}
\land c.verification.receipt \text{ is a nonblank string},
]

[
\operatorname{RevisionMatch}(c) \iff
c.verification.source\_revision = c.source\_revision.
]

Additional observed registry checks are: status must belong to (S); every non-`PROVED` claim must have a nonempty `boundary`; closure wording in `public_claim` is rejected unless status is `PROVED`; and phrases in `forbidden_promotions` are rejected in `public_claim`.

The negative tests independently exercise three `PROVED` rejection cases: nonempty `unresolved_obligations`, stale `source_revision`, and absent proof receipt. These tests establish those specific verifier behaviors; they do not establish exhaustive transition coverage.

### Proposed transition relation (specification, not implemented)

Let (C) be the set of claim records and (S\) the allowed status set above. Define a candidate promotion request as a pair ((c,c')) where the claim identity is unchanged and the requested status changes to `PROVED`.

[
\operatorname{PromoteToProved}(c,c') \iff
c'.id=c.id
\land c'.status=PROVED
\land c.status\in S\setminus\{PROVED\}
\land \operatorname{AdmitProved}(c').
]

This is a *proposed gate relation* derived from the observed snapshot predicate. The current Python verifier does not implement this relation: it validates a registry snapshot and does not receive or compare a pre-state and post-state. Consequently, it cannot currently enforce the source-status condition, immutable identity, authorized transition path, or transition-history recording.

### Preconditions and prohibited cases

| Gate condition | Required for candidate `PROVED` promotion | Current implementation evidence |
|---|---|---|
| Status vocabulary | Source and target statuses belong to the six-value allowlist; source is not already `PROVED` for a promotion event. | Allowlist checked; source-state/event semantics not checked. |
| Open obligations | `unresolved_obligations` is empty. | Checked; negative test exists. |
| Evidence presence | `evidence` is nonempty. | Checked; evidence is not semantically typed. |
| Proof receipt | `verification` is an object with a nonblank string `receipt`. | Checked; negative test for missing receipt exists. |
| Revision freshness | Receipt `source_revision` equals claim `source_revision`. | Checked; stale-revision negative test exists. |
| Claim/evidence binding | Receipt identifies the exact claim ID, proposition/version, scope, assumptions, and proof artifact digest. | Not checked by inspected verifier. |
| Proof validity | Proof artifact is independently verified by the appropriate proof checker and its result is bound into the receipt. | Not checked by inspected verifier. |
| Assumptions | No unresolved assumptions remain, or each assumption is explicitly discharged under the claim's declared semantics. | The inspected Core verifier checks `unresolved_obligations`, not a separate assumptions field. |
| History and authority | Promotion event records prior status, new status, actor/authority, timestamp, policy version, receipt, and source revision; unauthorized or duplicate transitions are rejected. | Not checked by inspected verifier. |
| Downgrade/invalidation | A change to claim text, scope, assumptions, dependencies, or source revision invalidates or reopens affected proof status. | Only source-revision mismatch is checked on a `PROVED` snapshot; automatic invalidation is not implemented. |

At minimum, the gate must reject: any `PROVED` target with an open obligation; absent/blank receipt; stale revision; empty evidence; invalid status; non-`PROVED` record without a boundary; and prohibited public-claim wording. The stronger intended system must additionally reject a receipt for a different claim or proposition, a proof that does not cover the declared scope/assumptions, an unauthorized transition, and reuse of stale evidence after claim mutation. These latter cases are specification requirements, not verified current behavior.

### Comparison against assurance cases

Assurance-case methods already structure top-level claims, subclaims, arguments, assumptions, and supporting evidence. The SEI's 2024 Experiment Zero report describes assurance cases as arguments decomposing claims into subclaims and connecting them to evidence; it also discusses formalizing arguments and processing them with verification tools, including change-aware recertification. This is substantial prior art against any broad claim that machine-processable claim/evidence structure or automated assurance reasoning is new.

The plausible difference is narrower: a research-claim status gate that treats `PROVED` as a controlled epistemic state and rejects promotion unless claim-specific proof receipt, revision freshness, and obligation-closure conditions are satisfied. Even this difference is not established: argument-driven certification and formal assurance work may implement related lifecycle constraints, and a full-text semantic comparison remains necessary.

### Comparison against policy-enforcement systems

Open Policy Agent (OPA) explicitly separates policy decision-making from enforcement: structured input is evaluated against declarative policies, and the host system enforces the returned decision. Cedar similarly evaluates a principal/action/resource/context request against policies, applies default-deny and forbid-overrides-permit rules, and returns a decision with diagnostics. These systems establish strong prior art for machine-readable policy, deterministic allow/deny decisions, schema validation, and externalized policy enforcement.

Therefore, a generic claim to an executable promotion policy, a deny-on-failed-precondition rule, or policy-as-code is not a novelty basis. The potentially distinctive domain semantics would have to be the exact research-claim transition model: claim identity and scope binding, typed proof receipts, assumption/obligation discharge, source-revision invalidation, and epistemic status history. The current URF Core validator implements only a subset of these conditions.

### Revised novelty assessment

| Candidate contribution | Updated assessment |
|---|---|
| Machine-readable claim/evidence structure | Strong overlap with assurance-case and structured argument models; not novel as a general concept. |
| Automated evaluation of a rule and rejection on failure | Strong overlap with OPA/Cedar policy enforcement and formal assurance tooling; not novel as a general mechanism. |
| `PROVED` admission predicate requiring no unresolved obligations, evidence, a receipt, and matching source revision | Concrete implemented subset in URF Core; domain-specific combination may be worth comparing, but novelty remains unresolved. |
| Transition-history enforcement and automatic invalidation after claim mutation | Not demonstrated in the inspected verifier; cannot be claimed as implemented or novel. |
| Claim-bound, independently checked proof receipts | Not demonstrated in the inspected verifier; remains a required specification gap. |

### Preserved boundaries

`BOUNDARY :=` The richer claim-governance package's complete schema and verifier have not been recovered in this audit; the URF Core verifier is related implementation evidence, not proof that both packages share identical semantics.

`BOUNDARY :=` The inspected verifier validates registry snapshots; it does not implement an explicit state-transition engine.

`BOUNDARY :=` The inspected verifier does not independently verify proof artifacts or bind a receipt to the exact claim proposition, claim scope, or proof digest.

`BOUNDARY :=` Novelty relative to assurance cases, formal assurance argument systems, OPA, Cedar, and adjacent lifecycle/provenance systems is not established.

`BOUNDARY :=` The indicator-validity, unreproduced 10,000-trial sensitivity analysis, incomplete negative-test coverage, and LaTeX presentation warnings recorded above remain open.

### Next bounded improvement

Recover the richer package's exact schema and verifier source before claiming that the candidate relation above describes that package. Then implement or formally specify a transition API that takes an immutable pre-state and proposed post-state, checks claim identity/scope and proof-receipt binding, and records a versioned promotion event. Add one negative test per prohibited transition before any novelty conclusion.
