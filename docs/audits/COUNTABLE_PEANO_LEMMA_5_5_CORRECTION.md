# Lemma 5.5: clarified boundary-value audit and local repair

**Reference:** Jeremy Brazas and Petar Pavešić, *Countable Models of One-Dimensional Peano Continua*, arXiv:2610.35875v1, Lemmas 4.3, 5.2, 5.4, 5.5, pp. 6–10. Source: https://arxiv.org/pdf/2610.35875

**Scope:** One audit finding and a proposed mathematical repair. This is NOT a counterexample to Lemma 5.5 or the paper's main theorem. It is NOT a Lean-verified result. No further claims about the paper are inferred.

## 1. Author clarification received on 2026-10-31

Jeremy Brazas explained that two occurrences of `A_n` in the third paragraph of Lemma 5.5 should read `B_n`, and that the intended extension uses the topological boundary
`∂U = cl(U) \ int(U)` and the *closed* domain `cl(U(b_n))`. This agrees with what is already printed on p. 9. The previous audit's purported closure-domain objection was mistaken; it is withdrawn.

## 2. Independent boundary-value issue

Write `C_0 = A ∪ B_0`, `U = g^{-1}({b_n}) \ A` (open in the metrizable domain `B`), `Z = cl_B(U)`, and `F = ∂_B U = Z \ U`. As in the proof, `F ⊆ C_0` and `k : C_0 → X` is continuous.

The printed inference
`g(F) ⊆ {a_n,c_n}`
is not implied by the lemma's hypotheses: a boundary point in `A` may have `g=b_n`, and its prescribed value `f` may lie in the interior `B_n`.

A concrete instance is `B=[0,1]`, `A={0}`, `g(t)=b_n` constantly, and `f(0)=y` for any `y∈B_n`. Then `U=(0,1]`, `F={0}`, and `g(F)={b_n}`, contradicting the claimed endpoint inclusion, while `q∘f=g|_A` holds.

What does follow is
`g(F) ⊆ cl_{C X}({b_n}) = {a_n,b_n,c_n}`, so
`k(F) ⊆ q^{-1}({a_n,b_n,c_n}) = cl_X(B_n)`.
This weaker statement is sufficient. The analogous statement holds for `d_n` and `cl_X(D_n)`.

## 3. Generalized local extension (proved at the level of point-set topology)

Choose a homeomorphism `θ : cl_X(B_n) → [0,1]` taking `a_n,c_n` to `0,1`, and define `h_F=θ∘k|_F : F→[0,1]`. The metric space `Z` is normal, and `F` is closed in `Z`. By the bounded Tietze extension theorem, `h_F` extends to a continuous `H : Z→[0,1]`.

If `F ≠ ∅`, let
`r(z)=dist(z,F)/(1+dist(z,F))`
and
`E(z)=(1-r(z))H(z)+r(z)/2`.
Then `E|_F=h_F` and `0<E(z)<1` for every `z∈U`. If `F=∅`, define `E≡1/2` on `Z=U`.

Thus `L_n=θ^{-1}∘E : Z→cl_X(B_n)` is continuous, agrees with `k` on `F`, and sends `U` into `B_n`. Consequently `q∘L_n=g` on `U` (both sides equal `b_n`). The identical construction with `cl_X(D_n)` works for `U(d_n)`.

This repair uses Tietze rather than applying Lemma 5.4 to potentially non-endpoint-valued boundary data.

## 4. Sequential continuity of the assembled lift

Define `\tilde g` on `C_0` by `k` and on each open `U(b_n)` / `U(d_n)` by the corresponding `L_n`. This is a well-defined lift. For each fixed index `n`, the map is continuous on the union of the closed sets `C_0`, `cl(U(b_n))`, and `cl(U(d_n))` by the finite pasting lemma: the overlaps are boundaries, and the maps agree there.

For any convergent sequence `s_j→s`, continuity is immediate along subsequences lying in `C_0` or pieces drawn from a bounded set of indices. To handle unbounded indices, pass to a subsequence whose associated indices `n_j` strictly increase, with `s_j∈U(b_{n_j})∪U(d_{n_j})`. Since `{b_m}` and `{d_m}` are open and `q(O_m)={b_m,c_m,d_m}` is an open neighborhood of `c_m`, continuity of `g` rules out `g(s)` being any `b_m,c_m,d_m`. Hence `g(s)=x∈w(X)`; the base map takes `s` to `x`.

Fix `ε>0` and choose a path-connected open neighborhood `W` of `x` contained in the metric ball `B_X(x,ε/2)`. By Lemma 5.2, `q(W)` is open; it is path-connected since `W` is. Because `g(s_j)→x`, eventually `g(s_j)∈q(W)`. The endpoint separation property used in the paper then gives `p_j∈W∩{a_{n_j},e_{n_j}}` for all such `j`.

The repaired local maps keep `\tilde g(s_j)∈B_{n_j}∪D_{n_j} ⊆ cl_X(O_{n_j})`. Since `p_j∈cl_X(O_{n_j})`, Lemma 4.3 implies
`dist_X(\tilde g(s_j),x) ≤ diam(cl_X(O_{n_j}))+dist_X(p_j,x) < ε`
for all sufficiently large `j`. Therefore `\tilde g(s_j)→x=\tilde g(s)`. Metrizability of `B` gives sequential continuity.

This supplies the infinite-gluing step using the diameter-shrinking lemma directly. The earlier diagonal-neighborhood argument is not needed for this completion.

## 5. Verification and communication boundaries

- **CORRECTED:** the earlier supposed closure-domain mismatch is withdrawn in light of the printed proof and the author's explanation.
- **MATHEMATICAL CHECK:** the endpoint-valued boundary assertion is contradicted by the explicit constant-map example; the generalized Tietze extension preserves prescribed boundary values and maps interiors into their required open arcs.
- **MATHEMATICAL CHECK:** continuity reduces to finite closed-piece pasting and the stated shrinking-diameter / endpoint-separation argument.
- **NOT VERIFIED IN LEAN:** prior Actions run 40991467393 failed in `CountablePeano/LocalExtension.lean`. No formal proof, compiler success, or axiom-audit receipt is claimed.
- **DO NOT PROMOTE:** neither falsity of Lemma 5.5 nor any objection to the main theorem follows.
- **AUTHOR FOLLOW-UP:** thank Jeremy for correcting the original objection; ask only about boundary points in `A` mapped to `b_n` and offer the generalized extension above. Avoid asserting a fatal defect.
