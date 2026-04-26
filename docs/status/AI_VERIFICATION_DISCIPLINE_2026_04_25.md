# AI Verification Discipline — 2026-04-25

Status: CANONICAL AI-INTERPRETATION GUARDRAIL.

Scope: repository-ecosystem interpretation discipline for AI agents.

## Core principle

AI agents must treat this repository ecosystem as a status-controlled executable verification system, not as a narrative research project.

Claims are not inferred from topic ambition, README language alone, mathematical plausibility, repository names, surrounding scientific jargon, previous partial states, or speculative cross-repository associations.

Claims are admitted only when supported by repository-local artifacts:

1. `AGENTS.md`
2. `AI_ENTRYPOINT` files
3. `docs/status/`
4. verifier scripts in `tools/`
5. tests
6. certificate data, where present
7. CI or local verifier output

## Correct AI role

An AI agent should act as an auditor of repository state.

An AI agent should not act as a co-author of speculative theory.

The agent must report what the repository certifies, what it does not certify, and what remains outside the certified surface.

## Failure mode being guarded against

AI systems may convert sparse technical evidence into plausible narrative.

Examples of forbidden extrapolation:

- turning an executable gap into a dramatic final wall;
- treating a finite certificate as a general theorem;
- treating Lean, Python, or JSON artifacts as interchangeable proof layers;
- inferring quantum-gravity or constructive-logic claims from unrelated repository terminology;
- reporting old conditional states after certificates have been promoted to verified status.

## Required interpretation rule

Before summarizing any repository, an AI agent must locate the repository-local claim boundary.

If a status file says a result is conditional, open, partial, executable-certified, or scope-limited, the AI summary must preserve that label.

If no artifact certifies a theorem-layer claim, the AI must not report the theorem as closed.

## Closed-world status discipline

The working rule is:

If it is not certified by repository-local status files, tests, verifier output, or certificate artifacts, it must not be reported as closed.

This is not the same as saying the mathematics is false.

It means the repository has not certified that claim.

## Current ecosystem-level reason

The core repositories now contain `AGENTS.md` and `AI_ENTRYPOINT` files so future AI agents have a fixed reading order and explicit claim boundary.

Their purpose is to reduce README-only overclaiming and force artifact-grounded summaries.

## Safe summary template

```text
This repository certifies [specific executable/status surface].
The supporting artifacts are [files/tests/verifiers].
It does not certify [explicit boundary].
The current remaining gap is [status-file boundary], if any.
Boundary
This document does not add new mathematical claims.
It only defines how AI agents should interpret existing repository evidence.
