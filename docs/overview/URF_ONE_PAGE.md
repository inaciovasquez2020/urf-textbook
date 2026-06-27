# Unified Rigidity Framework — One-Page Overview

## Reader Contract: What URF Claims and Does Not Claim

URF should be read as a bounded verification discipline, not as a claim of universal theorem closure.  A URF object is admissible only when its hypotheses, certificates, failure modes, and verification surface are all explicitly named.  The method is designed to preserve the difference between three states:

1. **Verified boundary**: a local claim has a reproducible artifact, verifier, or proof surface that checks under the repository rules.
2. **Conditional bridge**: a later result may use the object only after naming the remaining assumption or input theorem.
3. **Frontier obstruction**: the current package records why the stronger claim is not yet available.

This distinction is part of the textbook discipline.  A chapter should not promote a frontier target into a theorem merely because a nearby certificate exists.  Each reusable claim must say what it consumes, what it proves, and what remains outside the verified boundary.

A minimal URF reading pass therefore asks four questions:

- What is the finite object under discussion?
- Which verifier, artifact, or proof surface supports it?
- Which assumptions remain external?
- What stronger statement is deliberately not claimed?

This contract is the main safeguard against overclaiming.  It lets the book accumulate structure while keeping every added layer auditable.

## Core Idea
URF studies limits of global reconstruction when only **local information**
and **bounded information transfer** are available.

Locality + finite capacity ⇒ structural rigidity.

## Canonical Mechanism

Local neighborhoods  
↓  
Finite information transfer per refinement step  
↓  
Limited ability to distinguish configurations  
↓  
Structural rigidity  
↓  
Global obstruction to reconstruction.

## Main Structural Objects

- FO^k local types
- cycle–overlap rank (COR)
- entropy-depth lower bounds
- capacity bounds for refinement processes

## Key Insight

Local refinement algorithms cannot always recover global structure.
When cycle complexity is high and information transfer is bounded,
the system exhibits rigidity that prevents full reconstruction.

## Repository Roles

urf-core  
Framework definitions and axioms.

urf-spine  
Canonical structural lemmas and invariant relationships.

chronos-urf-rr  
Computational experiments and reference implementations.

urf-textbook  
Exposition, examples, and conceptual synthesis.

## Current Status

Active research program with:

- journal submissions
- formal verification work
- computational experiments
- expanding documentation.

