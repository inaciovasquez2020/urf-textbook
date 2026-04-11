# Shadow Compatibility Map

## Predicate

Define
ShadowCompatible(P)
iff
there exists a finite terminal ceiling L_P > 0 and a quantity q_P such that

1. q_P(P) ⊂ [0, L_P),
2. sup q_P(P) = L_P,
3. the central statement of P is unchanged when “near-maximal” language is rewritten using Shadow(L_P).

## Strong

Operational Collapse
- ceiling: observer/discrimination capacity ceiling
- quantity: accessible information flow
- status: Strong

Viotropic Wall
- ceiling: terminal admissible operational-complexity threshold
- quantity: realized operational complexity density
- status: Strong

Exchange Force Phase I
- ceiling: ECC_crit
- quantity: ECC
- status: Strong

Radiative Rigidity
- ceiling: terminal admissible radiative/stiffness threshold
- quantity: effective radiative response parameter
- status: Strong

## Weak

Chronos / EntropyDepth
- ceiling: transcript/capacity saturation ceiling
- quantity: realized extraction/transcript load
- status: Weak
- note: interpretive boundary language only; not theorem-generating primitive

The Wall
- ceiling: admissibility/capacity ceiling
- quantity: realized refinement load
- status: Weak
- note: interpretive boundary language only; not a replacement for ED lower bounds

## NonNative

Cayley C^k Rigidity
- native object: definability/rigidity
- status: NonNative

Structural Zero
- native object: zero-limit / floor law
- status: NonNative

OS mass-gap frontier
- native object: positive spectral floor m > 0
- status: NonNative

## Dual operators

Define
ShadowOfZero(ε) := { x : 0 < x <= ε and x -> 0 }.

Define
GapFloor(m) := { x : x >= m }.

## Usage law

If P is Strong, Shadow(L_P) may be used as a reusable boundary operator.
If P is Weak, Shadow(L_P) may be used only as secondary interpretive language.
If P is NonNative, replace Shadow(L_P) by the correct dual object.

## Lock rule

Shadow of Infinity is not a universal primitive.
It is a reusable boundary operator only on ShadowCompatible modules.
