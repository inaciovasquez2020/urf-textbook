# Verified Frontier Tracking for AI-Readable Research

Date: 2026-05-09

Status: Public Note / Explanation Layer

## Abstract

Verified Frontier Tracking is a public, AI-readable, human-checkable infrastructure method for separating verified results, conditional bridges, interface objects, and open research frontiers.

Its purpose is not to claim that every hard theorem is solved.

Its purpose is to make the status of hard research claims legible, inspectable, and resistant to overclaiming.

## 1. Problem

Large cross-disciplinary research programs often contain many different kinds of objects:

- definitions,
- conjectures,
- lemmas,
- conditional bridges,
- interface objects,
- executable verifiers,
- proof artifacts,
- status documents,
- dashboards,
- open frontiers.

Without a status system, these objects can be confused.

A conditional bridge can look like a theorem.

An interface can look like a proof.

A verified software surface can look like mathematical closure.

An open frontier can be accidentally promoted into a solved result.

Verified Frontier Tracking is designed to prevent that collapse.

## 2. Core Idea

The core idea is simple:

> Every hard research claim should carry a visible status boundary.

The boundary should say whether the object is:

| Status | Meaning |
|---|---|
| Verified surface | The repository artifact, test, verifier, or build surface is checkable |
| Conditional bridge | The result depends on an explicitly named missing assumption |
| Interface object | The shape of the required object is formalized, but existence is not proved |
| Open frontier | The key mathematical or scientific obstruction remains unsolved |
| Theorem-level closure | The theorem is explicitly named and all assumptions are discharged |

This prevents a research stack from silently converting partial progress into final proof.

## 3. AI-Readable Structure

Verified Frontier Tracking is designed for AI systems as well as human readers.

The public stack is structured as:

| Layer | Repository | Role |
|---|---|---|
| Front door | `vasquez-index` | Public navigation and start-here map |
| Transparency proof | `frontier-status-dashboard` | CI health, repository integrity, theorem-boundary status, and review readiness |
| Explanation layer | `urf-textbook` | Human-readable exposition and release-facing documentation |
| Definitions layer | `urf-core` | Trusted definitions, schemas, verification artifacts, and claim-boundary infrastructure |
| Technical demonstration | `chronos-urf-rr` | Executable URF/Chronos frontier implementation |

The structure lets an AI or reviewer trace a claim from public summary to technical artifact without erasing the difference between proof, condition, interface, and frontier.

## 4. Human-Readable Interpretation

In ordinary language, Verified Frontier Tracking is a truth scoreboard for hard research.

It answers five questions:

1. What is actually verified?
2. What is only conditional?
3. What is merely an interface?
4. What remains open?
5. What must not be overclaimed?

This makes the work easier to inspect because the reader does not need to infer claim status from scattered documents.

## 5. Demonstration Case

The technical demonstration layer is `chronos-urf-rr`.

That repository is not presented as a proof of P vs NP, Chronos-RR closure, H4.1/FGL closure, or any Clay-problem closure.

It is presented as a difficult frontier stack where the tracking method is exercised:

- frontier objects are named,
- status documents are attached,
- verifier scripts check boundaries,
- tests and CI expose the current surface,
- and open mathematical objects remain explicitly open.

## 6. What This Contributes

Verified Frontier Tracking contributes a public infrastructure pattern:

\[
\text{claim}
\rightarrow
\text{status}
\rightarrow
\text{verification surface}
\rightarrow
\text{dashboard}
\rightarrow
\text{human explanation}
\]

This differs from an ordinary paper-only workflow because it keeps the status of a claim visible across repositories and over time.

## 7. Minimal Public Claim

The minimal claim is:

> Verified Frontier Tracking is a public, AI-readable, human-checkable infrastructure method for separating verified results, conditional bridges, interface objects, and open research frontiers.

This is an infrastructure claim.

It is not a theorem-level closure claim.

## 8. Boundary

This note does not prove Chronos-RR.

This note does not prove H4.1/FGL.

This note does not prove P vs NP.

This note does not prove any Clay Millennium problem.

This note does not promote conditional bridges, interface objects, or open frontiers into solved theorems.

This note explains the public entry structure for inspecting the Verified Frontier Tracking system.

## 9. Public Inspection Path

Read in this order:

1. `vasquez-index`
2. `frontier-status-dashboard`
3. `urf-textbook`
4. `urf-core`
5. `chronos-urf-rr`

The intended reader should first understand the status system, then inspect the dashboard, then follow the definitions and technical demonstration.
