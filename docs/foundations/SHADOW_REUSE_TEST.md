# Shadow Reuse Test

## Predicate

Define
ShadowCompatible(P)
iff
there exists a finite terminal ceiling L_P > 0 and a quantity q_P such that

1. q_P(P) ⊂ [0, L_P),
2. sup q_P(P) = L_P,
3. the central statement of P is unchanged when near-maximal language is rewritten using Shadow(L_P).

## Status output

- Strong
- Weak
- NonNative

## Output law

If P is Strong, Shadow(L_P) is reusable as a boundary operator.
If P is Weak, Shadow(L_P) is reusable only as secondary interpretive language.
If P is NonNative, replace Shadow(L_P) by the native dual object.

## Canonical machine-readable sources

- artifacts/spec/shadow_reuse_test.json
- artifacts/spec/shadow_reuse_test.toml
- artifacts/spec/shadow_reuse_cases.json

## Renderer

tools/render_shadow_reuse_cases.py renders md, txt, and tex outputs from the canonical JSON cases file.
