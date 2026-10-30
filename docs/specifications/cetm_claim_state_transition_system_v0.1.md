# CETM Claim-State Transition System (CSTS) v0.1
**Status:** New proposed specification; not part of the recovered manuscript's demonstrated implementation  
**Date:** 2026-10-30  
**Implementation status:** Not implemented; no conformance claim  
**Purpose:** Define deterministic, auditable transitions for research-claim status without conflating claim type, evidence, and publication wording.

## 0. Provenance and scope boundary

This document is a new specification authored after the reported original archives
\`urf_claim_governance_arxiv_v0.1.zip\` and
\`urf_claim_governance_arxiv_source.tar.gz\` could not be recovered. It is not a
reconstruction of either archive, not a claim about their contents, and not a
retroactive description of the manuscript or the URF Core snapshot validator.

The recovered manuscript defines the conceptual CETM tuple
\[
C=(N,S,A,V,B,F,P)
\]
and the partial condition
\[
\operatorname{PromoteAllowed}(C,S') \Rightarrow
\operatorname{Discharged}(A)\land
\operatorname{Supports}(V,S')\land
\operatorname{Compatible}(B,P).
\]
It does not define these predicates as executable functions or specify a complete
transition relation. CSTS v0.1 supplies one possible operational extension. It
must be evaluated as a new design, not represented as a feature already present
in CETM, the manuscript, or URF Core.

CSTS governs the declared epistemic and publication state of a claim record. It
does not prove mathematical propositions by itself. A trusted proof checker,
validated certificate checker, or other domain-appropriate verifier must supply
the underlying verification result.

## 1. Design principles

1. **Separate claim kind from epistemic state.** A theorem, interface claim,
   certificate, and frontier object are different kinds of objects. They must not
   be represented as a single ambiguous status ladder.
2. **Immutable identity per semantic version.** A proposition, formal scope,
   assumptions, or dependency change creates a new semantic version.
3. **No implicit promotion.** State changes occur only through named events and
   explicit preconditions.
4. **Fail closed.** Missing, malformed, stale, unverifiable, or ambiguously bound
   evidence cannot satisfy a promotion guard.
5. **Proof checking is external.** A receipt records a check performed by an
   identified checker; a receipt string alone is not proof.
6. **Append-only history.** Every accepted state-changing event is recorded.
   Current state is a deterministic projection of the event history.
7. **Publication language is gated separately.** A valid internal state does not
   authorize broader wording than the claim's scope and evidence support.
8. **No automatic truth inference.** A successful gate establishes conformance
   to this transition policy, not truth beyond the soundness assumptions of the
   named checker and formalization.

## 2. Data model

### 2.1 CETM compatibility layer

The original seven conceptual fields remain:

| CETM field | CSTS interpretation |
|---|---|
| \(N\) Name | Human-readable claim name |
| \(S\) Status | Derived publication-facing label; not freely writable |
| \(A\) Assumptions | Typed, individually identified assumptions with discharge state |
| \(V\) Verification surface | Typed evidence references and verification receipts |
| \(B\) Boundary locks | Structured non-claims, scope constraints, and wording restrictions |
| \(F\) Frontier objects | Explicit unresolved obligations and dependencies |
| \(P\) Publication language | Controlled phrases permitted by current state and scope |

CSTS does not silently redefine the original status taxonomy. It makes the
following separation explicit:

- \`kind\`: \`THEOREM\`, \`INTERFACE\`, \`CERTIFICATE\`, or \`FRONTIER\`.
- \`state\`: \`OPEN\`, \`CONDITIONAL\`, \`PROVED\`, \`INTERFACE_VERIFIED\`,
  \`CERTIFICATE_VERIFIED\`, or \`CLOSED\`.
- \`S\`: a derived label:
  - theorem + OPEN -> \`Frontier object\` only if the record represents a
    theorem target not yet established; otherwise the author must use a separate
    declared non-promoted label in publication metadata;
  - theorem + CONDITIONAL -> \`Conditional theorem\`;
  - theorem + PROVED -> \`Proven theorem\`;
  - interface + INTERFACE_VERIFIED -> \`Interface theorem\`;
  - certificate + CERTIFICATE_VERIFIED -> \`Certificate\`;
  - any record with an active status lock -> additionally carries a
    \`Status lock\` annotation, not a replacement state.

A \`FRONTIER\` kind is a tracked missing object, not a theorem that can be promoted
in place. When the frontier is discharged, it is closed and linked to the new
claim or artifact that resolves it. This avoids treating an unresolved lemma
record and the theorem it eventually supports as the same proposition.

### 2.2 Required claim record

Every record MUST contain:

- \`schema_version\`: exact CSTS schema version.
- \`claim_id\`: globally unique immutable identifier.
- \`semantic_version\`: positive integer, monotonically increasing per claim lineage.
- \`kind\`: one of the four values above; immutable within a lineage.
- \`state\`: one of the six values above.
- \`name\`: non-empty display name.
- \`proposition\`: exact human-readable proposition or artifact assertion.
- \`proposition_digest\`: SHA-256 of the canonical proposition representation.
- \`scope\`: machine-readable formal scope, including domain, objects, quantifiers,
  ambient structures, and exclusions as applicable.
- \`scope_digest\`: SHA-256 of canonical scope.
- \`assumptions\`: array of identified assumption records.
- \`frontier\`: array of identified unresolved-object records.
- \`evidence\`: array of typed evidence references.
- \`dependencies\`: exact claim IDs, semantic versions, and digests relied upon.
- \`boundaries\`: structured boundary locks and prohibited implications.
- \`publication_policy\`: allowed and prohibited phrases, with scope conditions.
- \`source_revision\`: repository URI, immutable commit/object ID, and relevant path
  or artifact identifier.
- \`created_event\`: event ID of registration.

All digests MUST be computed over a published canonical serialization
(UTF-8, Unicode NFC, deterministic object-key ordering, no insignificant
whitespace, explicit number/string/null rules). If canonicalization is not
implemented or cannot be reproduced, digest-bound promotion is disabled.

### 2.3 Assumption record

Each assumption MUST have:
- stable \`assumption_id\`;
- exact statement and statement digest;
- type: \`AXIOM\`, \`HYPOTHESIS\`, \`ENVIRONMENT\`, \`DEPENDENCY\`, or \`CONVENTION\`;
- status: \`OPEN\`, \`DISCHARGED\`, or \`EXPLICITLY_CONDITIONAL\`;
- supporting evidence IDs if discharged;
- discharge receipt if a formal or empirical check is required.

A theorem may enter CONDITIONAL only if every non-discharged assumption is
explicitly listed and the conditional proof receipt binds to the exact assumption
set. A theorem may enter PROVED only if every assumption required by the theorem
is discharged or is a declared foundational axiom accepted by the project's
published axiom policy. A hypothesis cannot be relabeled as an axiom merely to
pass the gate.

### 2.4 Frontier record

Each frontier item MUST have:
- stable \`frontier_id\`;
- exact missing statement / construction / estimate / data object;
- blocking relation: \`BLOCKS_PROOF\`, \`BLOCKS_SCOPE\`, \`BLOCKS_PUBLICATION\`,
  or \`INFORMATIONAL\`;
- status: \`OPEN\`, \`RESOLVED\`, or \`SUPERSEDED\`;
- resolver event and evidence reference when resolved or superseded.

Any OPEN frontier item with a blocking relation prevents PROVED promotion.
INFORMATIONAL items do not block proof status but must remain visible in
publication metadata.

### 2.5 Evidence and proof receipt

Evidence entries MUST be typed as one of:
\`FORMAL_PROOF\`, \`CHECKER_LOG\`, \`CERTIFICATE\`, \`TEST_RESULT\`,
\`DATASET\`, \`EXTERNAL_REFERENCE\`, or \`REVIEW_RECORD\`.

A proof receipt MUST contain:
- receipt ID and receipt schema version;
- claim ID and semantic version;
- proposition digest and scope digest;
- assumptions digest and dependency-set digest;
- source revision;
- proof artifact digest;
- checker name, version, executable/build digest, and configuration digest;
- checker result (\`PASS\` or \`FAIL\`);
- checker log digest;
- execution environment identifier;
- timestamp and signer/attestor identity.

A receipt is admissible only if its fields exactly match the current semantic
version and the checker is on the versioned trusted-checker policy list. A
non-empty receipt string, screenshot, CI badge, or self-authored assertion is
not sufficient. The gate records the checker's result; it does not independently
establish the checker's soundness.

## 3. State and transition semantics

Let a system state be
\[
\Sigma=(R,E,\Pi)
\]
where \(R\) is the map of current claim records, \(E\) is the append-only ordered
event log, and \(\Pi\) is the versioned policy/checker configuration.

An event \(e\) is accepted only if its schema validates, its actor is authorized
for that event, its expected prior version matches the current record, and all
event-specific guards hold. The transition function is partial:
\[
\delta:\Sigma\times Event\rightharpoonup\Sigma.
\]
If any precondition fails, \(\delta\) is undefined and the implementation MUST
return a structured rejection without mutating \(R\) or \(E\).

### 3.1 Event envelope

Every event MUST include:
- unique \`event_id\`;
- \`event_type\`;
- \`claim_id\`;
- \`expected_semantic_version\`;
- actor identity and role;
- timestamp;
- policy version;
- payload digest;
- previous-event hash and event hash;
- reason/rationale;
- authorization/approval references where required.

The event hash is computed over the canonical event envelope excluding its own
hash field. The event log MUST reject duplicate event IDs, broken hash links,
out-of-order sequence numbers, and unauthorized writes. A hash chain detects
alteration relative to a trusted checkpoint; it does not by itself prove who
created an event or prevent deletion of the entire log.

### 3.2 Allowed state transitions

The following table is exhaustive for v0.1. Any unlisted transition is prohibited.

| Kind | Source | Target | Event | Required guard |
|---|---|---|---|---|
| THEOREM | absent | OPEN | REGISTER | Required record fields valid; identity and scope defined |
| THEOREM | OPEN | CONDITIONAL | SET_CONDITIONAL | Conditional proof receipt passes and binds exact proposition, scope, assumptions, dependencies, revision |
| THEOREM | OPEN | PROVED | PROMOTE_PROVED | All PROVED guards in §4 pass |
| THEOREM | CONDITIONAL | PROVED | PROMOTE_PROVED | All PROVED guards in §4 pass; no unresolved conditional assumptions remain |
| INTERFACE | absent | OPEN | REGISTER | Interface proposition and exact interface scope defined |
| INTERFACE | OPEN | INTERFACE_VERIFIED | VERIFY_INTERFACE | Interface proof/test receipt binds exact interface proposition and scope |
| CERTIFICATE | absent | OPEN | REGISTER | Certificate assertion and validation policy defined |
| CERTIFICATE | OPEN | CERTIFICATE_VERIFIED | VERIFY_CERTIFICATE | Approved certificate checker passes on exact certificate digest |
| FRONTIER | absent | OPEN | REGISTER | Missing object and blocking relation defined |
| FRONTIER | OPEN | CLOSED | CLOSE_FRONTIER | Resolver evidence and linked successor claim/artifact supplied |
| Any non-withdrawn record | current state | WITHDRAWN | WITHDRAW | Authorized owner/maintainer; reason recorded |
| Any non-withdrawn record | verified state | OPEN | REVOKE_OR_REOPEN | Revocation reason, invalidation cause, and impacted dependencies recorded |
| Any record | current version | new semantic version | REVISE | New immutable version created; invalidation propagation rules in §5 applied |

No transition from WITHDRAWN is allowed. Reinstatement requires a new claim ID with an explicit \`supersedes\` link. INTERFACE_VERIFIED and CERTIFICATE_VERIFIED cannot be promoted to theorem PROVED; a distinct theorem claim must cite them as evidence/dependencies. FRONTIER cannot be promoted in place; closure links to a distinct resulting claim or artifact.

### 3.3 Non-state-changing events

The following may append events without changing epistemic state:
- \`ATTACH_EVIDENCE\`;
- \`ADD_ASSUMPTION\`;
- \`ADD_FRONTIER\`;
- \`RESOLVE_FRONTIER_ITEM\`;
- \`SET_BOUNDARY_LOCK\`;
- \`RELEASE_BOUNDARY_LOCK\`;
- \`UPDATE_PUBLICATION_POLICY\`;
- \`ADD_DEPENDENCY\`;
- \`REMOVE_DEPENDENCY\`;
- \`ANNOTATE\`.

Each event must still pass schema, authorization, version, and audit-log checks.
If it changes proposition, scope, assumptions, dependencies, or source revision
semantics, it is a semantic revision and MUST use REVISE instead.

## 4. PROVED promotion predicate

For a theorem record \(c\), define:

\[
\begin{aligned}
\operatorname{CanProve}(c,\Pi)\iff{}&
\operatorname{WellFormed}(c)\land
\operatorname{IdentityStable}(c)\land
\operatorname{ScopeClosed}(c)\\
&\land\operatorname{AssumptionsDischarged}(c,\Pi)
\land\operatorname{NoBlockingFrontier}(c)\\
&\land\operatorname{EvidenceNonempty}(c)
\land\operatorname{ReceiptValid}(c,\Pi)\\
&\land\operatorname{DependenciesCurrent}(c)
\land\operatorname{SourceRevisionMatches}(c)\\
&\land\operatorname{BoundariesCompatible}(c)
\land\operatorname{PublicationPolicyValid}(c,\Pi).
\end{aligned}
\]

The predicates have the following exact obligations:

- \`WellFormed\`: all required fields validate against the declared schema; no
  unknown status, duplicate IDs, malformed digest, or dangling internal reference.
- \`IdentityStable\`: claim ID and semantic version match the event's expected
  pre-state; proposition and scope digests are reproducible.
- \`ScopeClosed\`: formal statement, quantifier/domain scope, exclusions, and
  interpretation conventions are explicit enough for the selected checker.
- \`AssumptionsDischarged\`: every required assumption is discharged with
  admissible evidence or explicitly permitted by the axiom policy; no
  untracked premise is used by the proof.
- \`NoBlockingFrontier\`: no OPEN frontier item blocks proof or scope.
- \`EvidenceNonempty\`: at least one typed proof artifact and checker log are
  present; references resolve and their content digests match.
- \`ReceiptValid\`: checker result is PASS; receipt binds exact claim ID,
  semantic version, proposition, scope, assumptions, dependencies, source
  revision, proof digest, checker build, and log digest; checker is approved.
- \`DependenciesCurrent\`: every relied-upon claim is in an allowed current state
  at the exact version/digest named by the receipt; no dependency is withdrawn,
  stale, or invalidated.
- \`SourceRevisionMatches\`: the receipt's immutable source revision equals the
  claim's current source revision and the proof artifact was generated from it.
- \`BoundariesCompatible\`: no boundary lock contradicts the theorem statement,
  its scope, the evidence, or the proposed publication wording.
- \`PublicationPolicyValid\`: every proposed publication phrase is allowed for
  the current state and does not exceed scope or imply a locked-out result.

If any conjunct is false, unknown, unavailable, or not independently evaluated,
PROMOTE_PROVED is rejected. Unknown is not treated as true.

The gate establishes only that the configured checker accepted the proof object
for the formalized proposition under the recorded assumptions and policy. It
does not establish that the formalization captures the intended informal
mathematics, that axioms are appropriate, or that the checker/toolchain is
sound absent separate assurance.

## 5. Revision, invalidation, and dependency propagation

A semantic revision occurs when any of the following changes:
- proposition text or formal proposition;
- scope, quantifiers, domain, or exclusions;
- assumption statements or assumption status;
- dependency set or dependency versions;
- source revision in a way that changes the proof-relevant source;
- checker policy or formalization mapping used by the receipt.

A semantic revision MUST:
1. create a new semantic version; never overwrite the old version;
2. append a REVISE event referencing old and new digests;
3. mark all receipts bound to the old semantic version as non-current for the new version;
4. return the revised claim to OPEN, unless a fresh receipt is supplied and
   rechecked in a separate promotion event;
5. traverse the reverse dependency graph and mark every dependent claim as
   \`STALE\` in its derived validity projection;
6. require each affected dependent claim to be reopened and reverified before
   it can be used as a current PROVED dependency;
7. preserve the old version and events for audit.

A non-semantic metadata edit (for example, a typographical correction in a
display-only description) may preserve state only if canonical proposition,
scope, assumptions, dependencies, source revision, and receipt-bound digests
are unchanged. The implementation must prove that these digests are unchanged;
it cannot infer non-semanticity from a human label.

If a dependency is revoked, withdrawn, revised, or loses its verified state,
all dependent proofs whose receipts cite that dependency version become stale.
The propagation must be transitive and deterministic. Cycles in the dependency
graph are rejected unless a separate, explicitly specified mutual-dependency
semantics is introduced; v0.1 does not define one.

## 6. Boundary locks and publication language

A boundary lock is a structured rule containing:
- lock ID;
- protected claim/scope component;
- prohibited inference or phrase;
- reason;
- effective semantic versions;
- release authority and release evidence, if releasable.

A lock is active until a RELEASE_BOUNDARY_LOCK event satisfies its specified
authority and evidence conditions. A lock cannot be silently removed by editing
the record.

Publication phrases are evaluated against the current derived state:
- THEOREM/PROVED may use theorem/proved language only for the exact proposition
  and scope covered by the receipt.
- THEOREM/CONDITIONAL may use conditional language and must enumerate every
  remaining premise.
- INTERFACE/INTERFACE_VERIFIED may claim only the verified interface result.
- CERTIFICATE/CERTIFICATE_VERIFIED may claim only that the named certificate
  passed the named checker; it cannot imply a theorem unless a separate theorem
  claim is proved.
- FRONTIER/OPEN may describe the target as open, conjectural, missing, or under
  investigation; it may not use proved/established/solved language.
- WITHDRAWN may not be presented as current support.

The language gate is a policy check, not a general natural-language theorem
prover. Any phrase not recognized by the versioned phrase policy is routed for
human review and cannot be automatically approved as stronger wording.

## 7. Authorization and policy versioning

Roles in v0.1:
- \`AUTHOR\`: register and revise own claims; attach evidence; propose assumptions,
  frontier items, boundaries, and wording.
- \`VERIFIER\`: run or attest to approved checkers; cannot approve own proof
  receipt unless the policy explicitly permits independent self-checking (default:
  prohibited for promotion).
- \`REVIEWER\`: independently review proof/scope/assumption bindings and approve
  promotion where required.
- \`MAINTAINER\`: manage schema, checker allowlist, policy versions, and emergency
  revocation; cannot silently edit historical events.

For PROVED promotion, the default policy requires a verifier identity distinct
from the author and a reviewer approval distinct from both. A project may adopt
a weaker policy only through a versioned policy change that is visible in every
resulting receipt and report. Policy changes do not retroactively rewrite events;
they may trigger revalidation of affected records.

All decisions record the policy version and checker allowlist version used.
Policy rollback or checker revocation triggers a review of claims whose receipts
depended on the affected version.

## 8. Prohibited transitions and failure semantics

The following are always rejected in v0.1:
1. direct mutation of state without a named event;
2. PROVED promotion with any open blocking frontier item;
3. PROVED promotion with an open or untracked required assumption;
4. PROVED promotion with empty evidence, a blank receipt, or a receipt string
   lacking a verifiable structured payload;
5. use of a receipt for another claim, semantic version, proposition, scope,
   assumption set, dependency set, source revision, or proof digest;
6. proof receipt from an unapproved checker or checker version;
7. proof receipt whose result is FAIL, UNKNOWN, missing, or not reproducible;
8. PROVED promotion based only on a CI badge, test count, citation, external
   endorsement, or author assertion;
9. promotion of an INTERFACE, CERTIFICATE, or FRONTIER record to theorem PROVED;
10. editing a historical event or replacing an old semantic version in place;
11. use of stale, withdrawn, or invalidated dependencies;
12. removal or weakening of an active boundary lock without an authorized event;
13. publication wording broader than the exact verified proposition and scope;
14. duplicate event IDs, invalid hash chain, stale expected version, or
    unauthorized actor;
15. silent treatment of missing data or unknown predicate results as success.

Failure returns a machine-readable rejection with:
\`code\`, \`failed_guards[]\`, \`claim_id\`, \`expected_version\`,
\`observed_version\`, \`policy_version\`, and \`event_id\` (if assigned).
A rejected event leaves the current claim projection and accepted event log
unchanged. A rejection audit may be stored in a separate append-only security
log, clearly distinguished from accepted state-transition events.

## 9. Determinism and conformance requirements

A conforming implementation MUST:
- validate all input against a versioned schema;
- implement the exact transition table and all guards in §§3–8;
- use deterministic canonicalization and cryptographic digests;
- verify receipt-to-claim binding field by field;
- verify actor authorization and required separation of duties;
- maintain append-only, integrity-checked event history;
- reconstruct the same current state from the same initial state and accepted
  event sequence;
- propagate invalidation transitively through dependencies;
- reject unknown event types, unknown states, missing fields, and unknown guard
  outcomes by default;
- emit machine-readable acceptance/rejection receipts;
- provide a test suite covering every allowed transition and every prohibited
  case in §8;
- include mutation tests showing that changes to proposition, scope, assumptions,
  dependencies, source revision, proof digest, checker version, or policy version
  invalidate affected receipts as specified.

A schema validator alone is not a CSTS implementation. A snapshot validator that
checks a final record without comparing prior and proposed states is not a CSTS
transition engine. A transition engine without independent proof checking is
not a proof verifier.

## 10. Minimal acceptance test matrix

| Test | Input condition | Expected result |
|---|---|---|
| T01 | Register well-formed theorem | Accept OPEN |
| T02 | Conditional theorem with exact conditional receipt and explicit open assumptions | Accept CONDITIONAL |
| T03 | Conditional theorem with unlisted premise | Reject |
| T04 | Promote theorem with valid bound proof, discharged assumptions, no blocking frontier | Accept PROVED |
| T05 | Promote with open blocking frontier | Reject |
| T06 | Promote with blank/missing receipt | Reject |
| T07 | Reuse receipt for another claim ID | Reject |
| T08 | Reuse receipt after proposition or scope digest changes | Reject |
| T09 | Reuse receipt after assumption/dependency/source revision changes | Reject |
| T10 | Receipt from unapproved checker/version | Reject |
| T11 | Verify interface claim; attempt theorem promotion on same record | Reject |
| T12 | Verify certificate; infer theorem from certificate status alone | Reject |
| T13 | Close frontier with resolver evidence and linked successor | Accept CLOSED |
| T14 | Revise a proved claim | New version OPEN; old version preserved |
| T15 | Revise a dependency | Dependent claims become stale transitively |
| T16 | Remove active boundary lock without authority | Reject |
| T17 | Publish stronger wording than current state permits | Reject or human-review hold |
| T18 | Duplicate event ID or stale expected version | Reject |
| T19 | Rebuild state from same event sequence | Identical projection |
| T20 | Corrupt event hash link | Reject reconstruction / integrity alarm |

These are specification-level expected outcomes. No tests are claimed to have
been implemented or passed.

## 11. Comparison with established systems

This section is a preliminary mechanism-level comparison, not a novelty proof.

### 11.1 Assurance-case systems (OMG SACM / GSN family)

SACM already represents auditable claims, arguments, evidence, contextual
information, inferential/evidential links, counter-claims/counter-evidence, and
artifact references. Its scope overlaps heavily with CETM's claim, assumption,
verification-surface, boundary/context, and frontier concepts. It is therefore
not defensible to claim novelty for structuring claims and evidence, recording
context, or linking evidence to claims.

CSTS's proposed additional constraint is an operational status-transition
policy: state is derived from typed claim kind plus lifecycle state; promotion
requires a receipt bound to exact semantic version/scope/assumptions/dependencies;
and semantic revision invalidates dependent proof status. SACM's metamodel can
represent rich argumentation and evidence structures, but the cited SACM material
does not by itself establish that SACM lacks all possible workflow or
change-management implementations. The distinction is between a metamodel for
assurance arguments and this proposed transition policy, not a claim that SACM
cannot host such a policy.

### 11.2 Proof-carrying code / proof-carrying artifacts

Proof-carrying code already establishes the key pattern that an untrusted
producer supplies a formal proof tied to an artifact and a consumer checks that
proof against a declared safety policy before accepting the artifact. This is
strong prior art for typed proof artifacts, checker-mediated admission, and
producer/consumer separation.

CSTS applies a similar pattern to research claims: the object being admitted is
a versioned proposition with formal scope, assumptions, dependencies, and
publication boundaries rather than executable code satisfying a safety policy.
That domain shift alone does not establish novelty. A claim that CSTS adds
something distinctive would require a formal account of claim-version binding,
assumption discharge, dependency invalidation, and publication-language gating,
then comparison with proof-carrying data and proof-carrying artifact systems.

### 11.3 Policy enforcement (OPA and Cedar)

OPA already accepts structured input, evaluates declarative policy, and separates
policy decision-making from enforcement. Cedar already provides schema-aware
policy validation and explicit allow/deny authorization decisions, including
default-deny behavior. Therefore generic policy-as-code, schema validation,
deterministic allow/reject, and fail-closed evaluation are not novel CSTS claims.

CSTS could be implemented as a domain-specific policy evaluated by OPA, Cedar,
or another engine. The candidate contribution would reside in the exact
research-claim data model and transition semantics, not in the existence of a
policy engine. The comparison must test whether the proposed guards and
invalidation rules are genuinely additional domain semantics or merely a
straightforward encoding of an existing policy/workflow.

### 11.4 Provenance and event sourcing

Event sourcing already stores state-changing events as an ordered history from
which current state can be reconstructed, supporting auditability and
traceability. CSTS's append-only event log, event hashes, actor, timestamp,
policy version, and replay semantics therefore do not constitute a novel
provenance or event-history mechanism.

The proposed domain-specific addition is the rule that semantic changes to a
claim invalidate receipts bound to the old proposition/scope/assumption/dependency
version and propagate staleness through dependent claims. This must be compared
with existing build systems, configuration management, proof dependency
tracking, and assurance-case change-impact analysis before any novelty claim.

### 11.5 Comparison summary

| Mechanism | Established prior art | CSTS v0.1 candidate difference | Novelty result |
|---|---|---|---|
| Claim/evidence/context structure | SACM and GSN-style assurance cases | Research-specific status labels and publication controls | Overlap; not novel generally |
| Proof object checked before acceptance | Proof-carrying code/artifacts | Receipt binds proposition, scope, assumptions, dependencies, and source version | Strong analogy; distinctness unproved |
| Declarative allow/reject policy | OPA, Cedar | Domain-specific promotion and wording guards | Generic mechanism not novel |
| Immutable event history | Event sourcing/provenance systems | Claim-semantic invalidation and transitive proof staleness | Candidate rule; compare change-impact prior art |
| Publication-language boundary gate | Transparency/assurance reporting and policy systems | Explicit mapping from claim state/scope to allowed phrases | Candidate integration; not yet compared exhaustively |

**Novelty status: NOT ESTABLISHED.** This specification is more precise than the recovered manuscript's
partial promotion condition, but precision and implementation intent do not
establish originality. A broader search and direct feature-level comparison are
required, especially for assurance-case lifecycle tooling, proof-carrying data,
proof dependency tracking, workflow/state-machine engines, and provenance-aware
change-impact systems.

## 12. Implementation boundary and next validation gates

CSTS v0.1 is a specification only. It has no executable schema, validator,
transition engine, trusted checker registry, test results, CI run, or external
replication result. It must not be described as implemented, verified, proved,
or novel.

Before implementation:
1. Freeze this specification and resolve review comments through a new version.
2. Define the canonical JSON serialization and JSON Schema.
3. Formalize \`delta\` and every guard in a proof assistant or executable reference
   model; prove determinism and fail-closed properties.
4. Implement a reference transition engine and a separate receipt verifier.
5. Test all T01–T20 cases plus adversarial mutation and authorization tests.
6. Compare the frozen semantics against SACM/GSN tooling, proof-carrying data,
   OPA/Cedar encodings, event-sourced workflows, and proof/build dependency
   invalidation.
7. Only after independent review may any novelty statement be considered.

## 13. References

- Object Management Group, [Structured Assurance Case Metamodel (SACM) 2.1](https://www.omg.org/spec/SACM/2.1/PDF), especially the argumentation and artifact metamodels.
- Necula, G. C. (1997), [Proof-Carrying Code](https://doi.org/10.1145/263699.263712), POPL.
- Necula, G. C. and Lee, P. (1996), [Safe Kernel Extensions Without Run-Time Checking](https://static.usenix.org/publications/library/proceedings/osdi96/necula.html), OSDI.
- [Open Policy Agent documentation](https://www.openpolicyagent.org/docs), policy evaluation over structured input and separation of decision from enforcement.
- [Cedar policy validation](https://docs.cedarpolicy.com/policies/validation.html) and [Cedar authorization](https://docs.cedarpolicy.com/auth/authorization.html).
- AWS, [Event Sourcing pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing-pattern.html).

