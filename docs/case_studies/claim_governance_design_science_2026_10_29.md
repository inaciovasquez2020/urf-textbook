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


## Source-package recovery and schema reconciliation (2026-10-30)

### Recovered manuscript source

The Library contains the manuscript source `manuscript_final_submission.tex` (49,600 bytes; 558 rendered lines) and earlier source `URF_Systems_Methodology_Manuscript_Stronger.tex` (37,672 bytes), along with corresponding PDFs and submission ZIPs. The recovered submission archive `urf_systems_submission_package_stronger.zip` contains eight files: the manuscript TeX/PDF, cover-letter TeX/PDF, editor-brief TeX/PDF, illustrative scoring CSV, and README. It does not contain a machine-readable claim schema, claim example, verifier, or tests. The separate main-text-only ZIPs contain only a TeX manuscript.

The final manuscript defines the CETM claim object as:

[
C=(N,S,A,V,B,F,P),
]

with these exact semantic fields:

| Symbol | Manuscript field | Meaning |
|---|---|---|
| (N) | Name | Stable identifier/name for the claim object |
| (S) | Status | Declared status from the manuscript's status taxonomy |
| (A) | Assumptions | Local assumptions required for the claim |
| (V) | Verification surface | Files, proofs, scripts, builds, tests, or artifacts supporting the status |
| (B) | Boundary locks | Explicit non-claims and no-overclaim statements |
| (F) | Frontier objects | Missing lemmas, estimates, invariants, data objects, or constructions |
| (P) | Publication language | Approved publication-facing verbs and phrases |

The manuscript's status taxonomy is: Proven theorem; Conditional theorem; Interface theorem; Certificate; Status lock; Frontier object. This is a distinct vocabulary from the six-value URF Core validator allowlist (`PROVED`, `RESTRICTED`, `CONDITIONAL`, `INTERFACE_ONLY`, `OPEN`, `NOT_CLAIMED`). The vocabularies must not be silently merged.

The manuscript's stated governance condition is:

[
operatorname{Promote}(C)	ext{ only if } A	ext{ is discharged, }
V	ext{ supports the promoted status, and }B	ext{ remains compatible with }P.
]

Its CBAL lifecycle is Register → Classify → Score → Scan → Block or Promote → Re-audit. It describes an ongoing governance loop, not a formal transition relation with typed event inputs and outputs.

### Reconciliation against the candidate promotion relation

The candidate relation previously written in this note used the URF Core snapshot fields and predicate:

[
operatorname{AdmitProved}(c) iff
c.status=PROVED
land c.unresolved_obligations=arnothing
land c.evidence
earnothing
land operatorname{ReceiptOK}(c)
land operatorname{RevisionMatch}(c).
]

That predicate is not a direct formalization of the manuscript CETM tuple. The fields map only partially:

| Candidate relation / verifier concept | CETM correspondence | Reconciliation |
|---|---|---|
| `status` | (S) | Direct semantic correspondence, but status vocabularies differ and require an explicit normalization map. |
| `unresolved_obligations` | (F) | Partial correspondence only. (F) is a set of frontier objects; it is not defined as a boolean or list of unresolved obligations, and not every frontier object necessarily blocks every status. |
| `evidence` | (V) | Partial correspondence. (V) is a verification surface that can list files, proofs, scripts, builds, tests, and artifacts; the manuscript does not define typed evidence records or a nonempty-evidence predicate. |
| proof receipt | (V) | No direct field. A receipt could be an implementation-level element of (V), but the manuscript does not specify receipt structure or matching semantics. |
| `source_revision` | No direct CETM field | Not specified in the seven-field tuple. It could be introduced as provenance/version metadata only by an explicit schema extension. |
| assumptions discharged | (A) | Direct conceptual correspondence. The manuscript states discharge as a promotion condition but does not define a machine-checkable discharge record or proof rule. |
| boundary compatibility | (B,P) | Direct conceptual correspondence. The manuscript requires compatibility but does not define a deterministic compatibility predicate or text-scanning semantics. |
| provenance and promotion history | No direct CETM field | Not present as explicit tuple components. The CBAL loop is longitudinal but does not specify immutable event records, actors, timestamps, or policy versions. |
| claim identity and scope binding | (N), with scope implicit in claim content | Stable name is specified; a globally stable ID, proposition digest, formal scope object, and mutation/invalidation rule are not specified in the CETM tuple. |
| epistemic status / mathematical scope | (S), (N), and claim content only indirectly | The richer-package summary used these terms, but the recovered manuscript's exact seven-field tuple does not define separate typed fields for epistemic status and mathematical scope. |

The CGRI's 16 indicators (S1–S4, A1–A4, V1–V4, B1–B4) are scoring dimensions, not additional claim-object fields. In particular, they do not supply a formal evidence receipt, transition history, source revision, or proof checker.

### Source and verifier recovery result

The exact richer-package archive previously reported as `/mnt/data/urf_claim_governance_arxiv_v0.1.zip` and source archive `/mnt/data/urf_claim_governance_arxiv_source.tar.gz` are not present in the current working container or searchable Library inventory. The prior conversation record reports that they were created, but it does not preserve their file listings, archive hashes, exact schema JSON, example JSON, verifier source, tests, or creation command output. The reported local paths therefore cannot be treated as currently recovered or verified artifacts.

No repository source corresponding to that richer schema/verifier was located in the inspected URF repositories. The URF Core validator source remains separately identifiable and does not establish the missing package's provenance or implementation.

### Corrected formalization status

The manuscript-level promotion rule can be represented only as a partial admissibility condition:

[
operatorname{PromoteAllowed}(C,S') Rightarrow
operatorname{Discharged}(A)
land operatorname{Supports}(V,S')
land operatorname{Compatible}(B,P).
]

The predicates (operatorname{Discharged}), (operatorname{Supports}), and (operatorname{Compatible}) are not defined executable functions in the recovered manuscript. There is no defined transition domain, allowed source/target status table, event record, or deterministic failure semantics. Therefore this implication is a faithful abstract restatement, not an executable specification.

### Preserved boundaries

`BOUNDARY :=` The exact richer-package schema and verifier source have not been recovered; their prior reported creation is not independently reproducible from currently available artifacts.

`BOUNDARY :=` The recovered manuscript CETM schema is exactly the seven-field conceptual tuple (C=(N,S,A,V,B,F,P)); it does not establish separate machine-readable fields for epistemic status, mathematical scope, evidence type/result, provenance, or promotion history.

`BOUNDARY :=` The manuscript's CBAL loop and promotion condition do not define a complete transition system.

`BOUNDARY :=` The URF Core snapshot validator is a related but distinct implementation and must not be attributed to the richer manuscript package.

`BOUNDARY :=` No transition engine is implemented or claimed by this reconciliation. Novelty remains unestablished, and all prior empirical, sensitivity-analysis, negative-test, and presentation boundaries remain open.

### Next admissible action

Recover the exact prior-turn archives from the original execution environment or obtain them as user-supplied files. Verify their SHA-256 hashes and archive listings, then extract the schema, example, verifier, and tests verbatim. Only after that can a field-preserving mapping from CETM to the richer package be certified. Do not synthesize missing source files or retrofit the URF Core validator and label it as the richer package.


## Three-stage validation architecture and longitudinal publication study (2026-10-30)

### Validation stages

The manuscript's limitations and conclusion support a three-stage validation architecture. These stages answer different questions and must be reported separately.

| Stage | Validation question | Evidence required | Boundary |
|---|---|---|---|
| 1. Artifact reproducibility | Can an independent user recover the supplied inputs and reproduce the scoring arithmetic and structural-verifier behavior? | Original indicator-level CSV, JSON Schema, illustrative claim record, verifier source, tests, archive listings, cryptographic hashes, and reproducible execution receipt. | Reproducing arithmetic or verifier behavior does not validate author-scored indicator judgments, mathematical truth, construct validity, or reviewer utility. |
| 2. Independent replication | Can external raters apply the CGRI rubric, reconstruct CETM fields, and identify substantially the same boundary locks and frontier objects? | Preregistered or otherwise version-locked rubric; independent raters; raw ratings and field reconstructions; inter-rater agreement and disagreement analysis; adjudication protocol. | Agreement supports reproducibility of the governance assessment, not mathematical correctness or publication impact. |
| 3. Longitudinal publication-outcome evaluation | Do manuscripts with explicit claim-governance artifacts make scope, assumptions, limitations, and remaining frontier objects easier for reviewers to identify than comparable manuscripts without those artifacts? | A defined manuscript cohort and comparison strategy; consistent reviewer-legibility measures; longitudinal collection protocol; confounder handling; analysis plan; outcome and missing-data reporting. | This is a proposed empirical study. No effect on reviewer comprehension, acceptance probability, or publication outcomes has been demonstrated. |

### Stage 3: proposed research design

The primary outcome should be reviewer ability to identify and correctly characterize:
1. the manuscript's claim scope;
2. assumptions required for each principal claim;
3. stated limitations and explicit non-claims; and
4. unresolved frontier objects or remaining proof obligations.

A secondary outcome may measure reviewer effort or time required to locate and interpret those elements, provided the measurement procedure is standardized. Acceptance, rejection, revision, and time-to-decision may be collected as exploratory publication outcomes, but they should not be treated as direct measures of governance quality.

A defensible comparison requires a defined sampling frame and a prespecified assignment or matching strategy. Where feasible, use randomized presentation of otherwise comparable manuscript versions, with and without the governance artifacts, to isolate their effect on reviewer legibility. If randomization is infeasible, use a matched observational cohort and explicitly address confounding by field, venue, manuscript maturity and quality, reviewer expertise, review process, and publication period. Do not interpret an uncontrolled difference in acceptance rates as a causal effect of CGRI or CETM.

The protocol should define:
- eligibility criteria, unit of analysis, sample size rationale, and observation window;
- the exact artifact intervention and control condition;
- reviewer instructions and a blinded scoring rubric where feasible;
- inter-rater reliability and adjudication procedures;
- primary and secondary endpoints, missing-data handling, and statistical analysis;
- ethics, consent, confidentiality, and data-retention requirements; and
- versioning of the CGRI rubric, CETM schema, and analysis code.

The central hypothesis is limited to reviewer legibility: explicit governance artifacts may improve reviewers' ability to identify scope, assumptions, limitations, and unresolved work. The study must not presume that the hypothesis is true. Increased acceptance probability is neither guaranteed nor implied; any association with acceptance would require separate analysis and careful causal qualification.

### Reproducibility-package obligations

The manuscript's Data Availability Statement explicitly promises the following four supplementary artifacts:

| Required artifact | Required verification | Current status in this recovery audit |
|---|---|---|
| Indicator-level scoring CSV | Recover original bytes; compute SHA-256; inspect exact rows and columns; reproduce reported scoring arithmetic without rounding or reconstruction. | A separately recovered CSV and its reported hash are documented above; its identity with the missing archive member has not been established. |
| JSON Schema | Recover original bytes; validate syntax; inspect required properties, types, enumerations, constraints, and schema version. | Not recovered from the reported archives. |
| Illustrative claim record | Recover original bytes; validate against the exact recovered schema; preserve all original values and semantics. | Not recovered from the reported archives. |
| Structural verifier | Recover source and tests verbatim; inspect dependencies and invocation; run the original tests against the original example and schema; record exact logs and hashes. | Not recovered from the reported archives. |

The two reported archive files remain unavailable in the active execution and Library inventory. The prior execution record supplies output paths but not the binary bytes. Accordingly, no archive hash, member listing, extraction, or original-source comparison is claimed. The separately inspected URF Core snapshot validator is not a substitute for the promised structural verifier.

### Updated conclusions and boundaries

The manuscript's current case study remains author-scored and illustrative. Recomputed scoring arithmetic, if reproduced from the recovered CSV, would establish arithmetic reproducibility only. It would not independently validate indicator judgments or show that the CGRI measures reviewer legibility.

Independent replication is the next validation stage capable of moving the method beyond an author-centered demonstration. Longitudinal publication-outcome evaluation is a subsequent, distinct stage and should prioritize reviewer-legibility outcomes over acceptance rates.

`BOUNDARY :=` Stage 1 is incomplete until the original schema, illustrative claim record, verifier, tests, and archive provenance are recovered and checked; a CSV alone is insufficient.

`BOUNDARY :=` Stage 2 has not been conducted; no external-rater agreement or inter-rater reliability result is established.

`BOUNDARY :=` Stage 3 is a proposed research design only; no longitudinal reviewer or publication-outcome data have been collected or analyzed.

`BOUNDARY :=` No claim is made that CGRI or CETM increases acceptance probability, guarantees acceptance, or improves mathematical correctness.

`BOUNDARY :=` The proposed three-stage validation architecture does not change the manuscript's novelty status, the author-scored status of the case study, or any previously recorded open boundary.


## Full-text prior-art audit and corrected novelty boundary (2026-10-30)

### Scope of this pass

This pass inspected the full accessible texts of FEDS (Venable, Pries-Heje, and Baskerville, 2016), *Validity in Design Science* / the Design Science Validity Framework (Larsen et al., 2025), and *Transparency in Design Science Research* (Hevner et al., 2024). It upgrades the earlier abstract-level matrix for these three works. It is still a bounded comparison, not a systematic search of all claim-management, assurance-case, workflow, policy, provenance, or proof-carrying systems.

### Full-text findings

**FEDS — evaluation strategy, not merely a checklist.** FEDS explicitly connects evaluation goals to strategies; its dimensions are formative/summative purpose and artificial/naturalistic paradigm. It describes four prototypical strategies, possible hybrid strategies, and a four-step process for choosing goals, strategies, properties, and evaluation episodes. Its account of artificial evaluation expressly includes mathematical proofs, theoretical arguments, simulations, laboratory experiments, and criteria-based analysis. Accordingly, neither evaluation planning, iterative evaluation trajectories, nor the use of mathematical proof as an evaluation method can be claimed as a URF novelty. FEDS is concerned with evaluating design artifacts and design theories; the reviewed text does not specify a claim-object status transition engine or an executable admission predicate for a research claim's epistemic status.

**Design Science Validity Framework (DSVF) — explicit claim-to-validity-to-evidence reasoning.** The full paper explicitly defines design-science validity as the extent to which knowledge claims about a focal artifact are supported by evidence. It distinguishes criterion, causal, and context claims/validities, defines subtypes, and directs the researcher to select an appropriate validity type for a stated claim and support it through a specified comparison. The paper states that design-science evaluations are comparisons and that its framework articulates the relationships among claim types and criterion, causal, and context validity. It also includes formal proof as an example of a validation method for a security protocol. This is substantial overlap with any broad URF claim that it uniquely structures claims, evidence, assumptions, or validation. The reviewed DSVF text provides a claim/validity/evidence reasoning framework and process; it does not specify the CETM tuple, a machine-enforced PROVED status transition, a receipt bound to a versioned proposition and proof digest, or deterministic invalidation rules. This last statement is limited to the reviewed framework text; it is not a claim about every implementation that might use DSVF.

**DSR Transparency — stronger process/provenance overlap than the abstract alone suggests.** The full text defines process transparency as communicating the actions used to generate artifacts and knowledge, including actual activity logs, reasons for activities/design choices, and context. It discusses process-capture tools and computational use of digital trace data. Its six transparency forms are process, problem space, solution space, build, evaluation, and contribution. The paper explicitly raises sharing data, artifacts, code, proofs, and subjective value judgments; discusses reproducibility and replication; and recommends documenting design decisions and evaluation evidence. Therefore, URF cannot claim to originate research-process logs, provenance documentation, transparent scope/assumptions, publication-facing evidence disclosure, or general artifact/proof sharing. The reviewed framework is transparency guidance and a conceptual framework; it does not specify a formal epistemic state machine or an executable promotion gate. Again, this is a bounded statement about the reviewed text, not a proof that no implementation or adjacent system has such a gate.

### Revised claim-by-claim matrix

| Proposed URF claim | FEDS full text | DSVF full text | DSR Transparency full text | Corrected status |
|---|---|---|---|---|
| A framework for planning evaluation episodes and trajectories | Direct: two evaluation dimensions, four strategies, hybrid strategies, four-step design process. | Related but different: selects validity reasoning appropriate to claims and comparisons. | Directly addresses evaluation transparency and reporting. | **Overlap; not novel.** |
| Explicitly connect claims to evidence and validation | Evaluation goals/properties are tied to evaluation episodes; mathematical proof is an admissible artificial evaluation method. | Direct and strong: claim types map to validity types and comparison evidence. | Directly asks for transparent assumptions, scope, processes, data, results, analyses, proofs, and implications. | **Strong overlap; not novel as a general concept.** |
| Record assumptions, scope, process, design decisions, and research boundaries | Context and goals are relevant to evaluation design, but not its central claim-object model. | Context claims and explicit knowledge claims bound where claims hold; evidence must support them. | Direct: problem-space scope, process activity/reasoning/context, and contribution transparency. | **Strong overlap in reporting/governance aims.** |
| Maintain activity provenance and process history | Evaluation trajectories record the planned progression of evaluation episodes. | Claim/evidence/validity argument is explicit; event-level history is not the framework's focus. | Direct: actual activity logs, reasons, context, digital trace data, and process-capture tools. | **Not novel as provenance or process logging.** |
| Store claim status, assumptions, verification surface, boundary locks, frontier objects, and publication language in CETM tuple C=(N,S,A,V,B,F,P) | No equivalent seven-field tuple identified in FEDS. | Claim and validity taxonomy overlaps semantically, but no equivalent tuple identified in the reviewed text. | Transparency dimensions overlap in content, but no equivalent seven-field claim-object tuple identified in the reviewed text. | **Candidate data-model difference only.** Exact schema and field semantics must be compared with assurance cases, argumentation models, and claim/provenance schemas. |
| Permit promotion only when assumptions are discharged, verification supports the target status, and boundaries remain compatible with publication language | No such CETM-style predicate identified; FEDS's evaluation planning is not itself this promotion rule. | DSVF requires evidence to support claims but does not define this exact status-admission predicate in the reviewed text. | Transparency guidance requires disclosure but does not define this exact status-admission predicate in the reviewed text. | **Candidate abstract governance rule, not an executable transition system.** The manuscript leaves Discharged, Supports, and Compatible undefined. |
| Enforce a PROVED transition using a claim-bound proof receipt, revision freshness, and obligation closure | Mathematical proof is an evaluation method; no corresponding claim-status gate identified in FEDS. | Formal proof can support validity evidence; no corresponding claim-status gate identified in the reviewed DSVF text. | Proof disclosure and process transparency overlap with the evidence/provenance inputs; no corresponding claim-status gate identified in the reviewed text. | **Not established in the manuscript or recovered package.** The separate URF Core snapshot validator implements only a partial admission check and is not a transition engine. |
| Record authorized promotion events and automatically invalidate status after claim mutation | Evaluation trajectories are not equivalent to an event-sourced claim lifecycle. | Claim-to-evidence validity does not itself specify immutable transition events or mutation invalidation. | Activity logs and trace-data capture are relevant prior art for recording process history. | **Unimplemented and unresolved.** A new event schema or invalidation rule cannot be claimed as an existing URF capability. |
| Show improved reviewer comprehension or publication outcomes | FEDS evaluates the utility of evaluation strategies; it does not validate this URF outcome claim. | DSVF requires explicit validity reasoning for such knowledge claims and suitable comparison evidence. | DSR Transparency is directly relevant to reviewer-facing disclosure and publication transparency. | **Not demonstrated.** The current author-scored illustrative case study is not an independent reviewer study. |

### Corrected novelty conclusion

The full-text comparison narrows, rather than strengthens, the novelty claim. FEDS, DSVF, and DSR Transparency already cover evaluation planning, claim/evidence reasoning, formal proof as evaluation evidence, explicit scope and assumptions, process documentation, provenance-like activity logs, and publication-facing transparency.

The recovered manuscript's actual CETM model is the conceptual seven-field tuple C=(N,S,A,V,B,F,P), accompanied by the partial promotion condition:

\[
\\operatorname{PromoteAllowed}(C,S') \\Rightarrow
\\operatorname{Discharged}(A) \\land
\\operatorname{Supports}(V,S') \\land
\\operatorname{Compatible}(B,P).
\]

The manuscript does not define the three predicates as executable functions, a source/target transition table, claim-version binding, proof-receipt schema, event log, actor authority, or automatic invalidation. Thus the strongest potential distinction is currently an **abstract claim-governance model with a stated promotion constraint**, not an implemented verification-first state-transition system. The richer package's reported schema/verifier archives remain unrecovered, so they cannot close this gap.

**Current novelty result: NOT ESTABLISHED.** A narrower contribution may become defensible if an exact executable transition semantics is recovered or specified and shown, through a broader comparison, to add a distinct capability beyond the claim/evidence validity reasoning, transparency/process capture, assurance-case argumentation, and policy/workflow enforcement already available. No claim is made that such a capability is unique at present.

### Primary full-text sources examined

1. Venable, J., Pries-Heje, J., & Baskerville, R. (2016). [FEDS: A Framework for Evaluation in Design Science Research](https://doi.org/10.1057/ejis.2014.36). *European Journal of Information Systems*, 25(1), 77–89. Full text: [Springer article](https://link.springer.com/article/10.1057/ejis.2014.36).
2. Larsen, K. R., Lukyanenko, R., Mueller, R. M., Storey, V. C., Parsons, J., VanderMeer, D., & Hovorka, D. (2025). [Validity in Design Science](https://doi.org/10.25300/MISQ/2024/18064). *MIS Quarterly*, 49(4), 1267–1294. Full text: [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC13004602/).
3. Hevner, A. R., Parsons, J., Brendel, A. B., Lukyanenko, R., Tiefenbeck, V., Tremblay, M. C., & vom Brocke, J. (2024). [Transparency in Design Science Research](https://doi.org/10.1016/j.dss.2024.114236). *Decision Support Systems*, 182, 114236. Full text: [author-uploaded corrected proof](https://www.researchgate.net/publication/380220169_Transparency_in_design_science_research).

### Remaining bounded work

1. Recover the original richer-package ZIP and TAR.GZ bytes; do not substitute the URF Core snapshot validator.
2. If recovery fails, treat the manuscript's seven-field CETM tuple and partial promotion condition as the complete currently evidenced URF specification.
3. Only then compare any proposed transition relation against assurance-case systems, proof-carrying claims, policy/workflow engines, and provenance/lifecycle systems using exact formal semantics rather than feature labels.
4. Keep independent indicator calibration, the unreproduced sensitivity analysis, broader negative tests, and LaTeX warnings open.
