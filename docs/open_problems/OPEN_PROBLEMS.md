# Unified Rigidity Framework — Open Problems

## Purpose

Record the principal open mathematical questions associated with the Unified Rigidity Framework (URF), with explicit frontier status boundaries.

## Core Open Problem

### Cycle–Local Rigidity

Fix \(k\) and \(\Delta\).

Find constants \(R(k,\Delta)\) and \(T(k,\Delta)\) such that every finite graph \(G\) with maximum degree \(\le \Delta\) satisfies

\[
\operatorname{COR}_{R}(G) \ge T(k,\Delta)
\Longrightarrow
G \text{ is not } FO^k_R\text{-homogeneous}.
\]

Equivalent formulations include:

- cycle-support rigidity;
- configuration pumping;
- overlap determinacy;
- hypergraph gadget rigidity;
- bounded-locality obstruction to global cycle-rank compression.

## Current Frontier Reduction

The global open problem is presently reduced to the construction or proof of a non-tautological admissibility object.

### Terminal Missing Object

Construct a finite, bounded-degree, graph-theoretic object satisfying the intended overlap-rigidity obligations:

1. a short-cycle boundary operator;
2. a local-cycle generation theorem;
3. a nontrivial quotient-rank bound;
4. an \(FO^k_R\)-type semantics map;
5. a proof that these obligations force type diversity.

Until this object is constructed, global Cycle–Local Rigidity remains open.

## Chronos / SiMSLV Status

Chronos SiMSLV is reduced to the weakest frontier lemma:

\[
\text{bounded local signatures}
\Longrightarrow
\text{non-tautological projected admissibility witness}.
\]

Current closed surface:

- finite envelope is certified;
- admissibility obligations are isolated;
- no unconditional Chronos closure is claimed.

Open object:

\[
\pi(D^{\mathrm{corr}}_{k,R,B}(P))
\supseteq
\operatorname{FourierSupp}(V_0)
\]

or an equivalent projected-character witness.

## CorrRank Status

CorrRank original-regime closure is reduced to non-tautological admissibility.

Closed surface:

- intended surface identified;
- finite-envelope instance certified;
- admissibility obligation surface isolated.

Open object:

\[
D^{\mathrm{corr}}_{k,R,B}(P)
\]

with a proof that its projected row span matches the intended type-measurable signature span.

## ORL Status

The intended graph-theoretic ORL frontier has been isolated.

Closed surface:

- intended cycle-boundary data;
- intended short-cycle-generation data;
- intended quotient-rank-bound data;
- intended \(FO^k_R\)-type semantics data;
- intended obligation package.

Open object:

\[
\mathrm{IntendedGraphTheoreticORLObligations}
\]

No global Overlap Rigidity theorem is claimed without this object.

## EntropyDepth Questions

1. Determine tight lower bounds for EntropyDepth on bounded-degree expanders.
2. Extend entropy non-amplification results to broader refinement models.
3. Characterize minimal entropy-loss mechanisms in local inference systems.
4. Prove that admissible bounded-support witnesses cannot simulate global transcript capacity.

## Structural Graph Questions

- Rigidity thresholds on random lifts.
- Cycle-overlap growth laws in sparse expanders.
- Interaction between expansion and \(FO^k\)-type diversity.
- Nontrivial quotient-rank lower bounds for local-cycle spaces.
- Exact relationship between short-cycle generation and global cycle-rank obstruction.

## Spectral Directions

- Relations between rigidity invariants and spectral gaps.
- Operator-theoretic interpretations of capacity bounds.
- Spectral certificates for local-cycle non-generation.
- Rank-stability under finite lifts and bounded local covers.

## Computational Directions

- Empirical measurement of rigidity thresholds.
- SAT or CSP instances exhibiting entropy-depth barriers.
- Algorithmic detection of cycle-overlap rank.
- Finite-patch certificate generation for projected admissibility witnesses.
- Exhaustive search for minimal non-tautological CorrRank / SiMSLV instances.

## Long-Term Goals

- formal proof of the Cycle–Local Rigidity principle;
- construction of the terminal ORL admissibility object;
- unified explanation of locality barriers in inference systems;
- cross-domain applications in complexity and physics;
- executable status locks preventing theorem-level overclaim.

## Boundary

This document records open problems and frontier reductions only.

It does not claim:

- unconditional Cycle–Local Rigidity;
- unconditional Chronos closure;
- unconditional CorrRank closure;
- unconditional Overlap Rigidity;
- a proof of \(P \ne NP\);
- a proof of any Millennium Prize problem.
