# Frontier Calculus

Status: Doctrine / Repository-Governance Layer

## Core Principle

A research repository can be complete without proving the target theorem, provided it certifies the smallest remaining obstruction.

Completion is not identical to solution.

Completion means:

1. The target is explicit.
2. The admissible methods are registered.
3. All weaker obstructions are handled.
4. The smallest surviving obstruction is named.
5. Future progress requires either:
   - a stronger negative closure certificate, or
   - a new separating invariant.

## Normal Form

A frontier-complete repository contains:

- TARGET.md
- METHOD_REGISTRY.json
- FRONTIER.md
- NEGATIVE_CLOSURE_CERTIFICATE.json

## Legal Transitions

A project may advance only by:

1. Solving the target theorem.
2. Shrinking the frontier.
3. Strengthening the negative closure certificate.
4. Introducing a new invariant that separates the current obstruction.

## Forbidden Transition

A repository must not mark an open theorem as solved merely because the surrounding artifact surface is complete.

## Canonical Slogan

Completion means the remaining gap has been made exact.
