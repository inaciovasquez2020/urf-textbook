# Source of Truth — 2026-04-27

Status: Documentation / Textbook Surface

This repository is a documentation, textbook, exposition, or synthesis surface. It does not independently prove mathematical claims. Any theorem status must inherit from a buildable formal repository and must use that repository's status label.

## Inheritance rule

Every theorem-level claim must point to:

- source repository
- commit or release identifier
- file path
- theorem or artifact name
- inherited status label

## Allowed inherited labels

- Verified
- Conditional
- Scaffold
- Quarantined Frontier
- Deprecated / Narrative
- Toy Verified Skeleton
- Toy Cardinality Model / Not a Real Bridge
- Clean Formal Scaffold / Needs Theorem Audit
- Placeholder / Scaffold

## Boundary rule

This repository must not claim independent theorem verification. Build success, LaTeX success, CI success, dashboards, ledgers, badges, or textbook exposition do not constitute theorem-level proof.
