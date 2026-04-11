# Shadow of Infinity

## Canonical status

Coined internal term.
Reusable only by fixed definition.
Not invoked as prior standard terminology.

## Master definition

Let L > 0 be a fixed terminal ceiling.

Define
Shadow(L) := { x in R : 0 <= x < L }.

An admissible shadow sequence for L is a sequence (x_n) such that
x_n in Shadow(L) for all n and x_n -> L.

Define
SoI(L) := (Shadow(L), L).

## Derived quantities

ShadowProximity_L(x) := L - x.
NormalizedShadow_L(x) := x / L.

## Canonical witness sequence

x_n := L(1 - 1/n).

Then
x_n in Shadow(L) for all n,
x_n -> L,
sup Shadow(L) = L,
L notin Shadow(L).

## Specializations

ShadowSpeed_c := Shadow(c).
ShadowDepth_D := Shadow(D).
ShadowEnergy_E := Shadow(E).

## Lock rule

Every manuscript using the term must define it explicitly on first use.
