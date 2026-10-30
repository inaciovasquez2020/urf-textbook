# Countable Peano lifting audit — Lean subproject

This is an isolated Mathlib project for the local endpoint-controlled extension
lemma arising in Lemma 5.5 of Brazas–Pavešić, arXiv:2610.35875.

It is deliberately separate from the root URF Lake configuration. It does not
modify the URF theorem library and does not claim a URF theorem.

## Scope

- CountablePeano/LocalExtension.lean: metric-space separator for two disjoint
  closed sets, with exact zero and one preimages.
- Not yet formalized: arc parametrization, the quotient model, the global
  lifting construction, infinite gluing, Serre fibration, or weak equivalence.

## Reproducible build

From this directory, with elan and Lake installed:

    lake update
    lake exe cache get
    lake build

The project pins both the Lean toolchain and the Mathlib dependency revision.
GitHub Actions runs the build and an axiom audit for the CountablePeano
namespace.

## Status boundary

A source file is not a verification receipt. The local lemma is not considered
Lean-verified until the pinned CI build and axiom audit pass.
