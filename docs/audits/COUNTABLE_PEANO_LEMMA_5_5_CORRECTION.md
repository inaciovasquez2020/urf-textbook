# Correction and completion note: Lemma 5.5 audit

**Paper:** Jeremy Brazas and Petar Pavešić, *Countable Models of One-Dimensional Peano Continua*, arXiv:2610.35875v1, Lemma 5.5, pp. 9–10.

This note supplements `COUNTABLE_PEANO_LEMMA_5_5_AUDIT.md`. It makes the local closure repair explicit and supplies the diagonal argument needed in the wild-point continuity case. It does not claim a counterexample to the lemma or theorem.

## 1. Exact domain mismatch

Write (U=U(b_n)=g^{-1}(b_n)\setminus A), with boundary taken in (B). The proof first establishes
[
\partial_B U\subseteq A\cup B_0,
]
then defines the boundary map (β=k|_{\partial_B U}). It next says that (\partial U) is closed in (U) and invokes Lemma 5.4 to obtain (h:U\to A_n) with (h|_{\partial U}=β).

For an open subset (U\subseteq B), (\partial_B U\cap U=\varnothing). Thus the ambient boundary is not a subset of the stated domain (U), and the displayed restriction is not defined. This is a literal domain mismatch in the printed proof. It is not a counterexample to the lifting statement.

## 2. A complete local repair using the paper's Lemma 5.4

Set
[
C=\overline U^{\,B},\qquad D=\partial_B U=C\setminus U.
]
Then (C) is a closed metrizable subspace of (B), and (D) is closed in (C). The map (β:D\to\{a_n,c_n\}) is continuous because it is the restriction of the continuous map (k) on (A\cup B_0). Its two endpoint fibres
[
E=\u03b2^{-1}(a_n),\qquad F=\u03b2^{-1}(c_n)
]
are disjoint closed subsets of (C).

Apply Lemma 5.4 with ambient space (C), closed subset (D), and endpoint-valued map corresponding to (β). It gives a continuous (r:C\to[0,1]) such that (r|_D) is the prescribed endpoint value and
[
r^{-1}(\{0,1\})=D.
]
Choose a homeomorphism φ from ([0,1]) onto the closed arc with endpoints (a_n,c_n), oriented so that the endpoint values agree with (β), and put (H=φ\circ r). Then (H:C\to\overline{B_n}) is continuous, agrees with (β) on (D), and maps (U=C\setminus D) into the open arc (B_n), since (r(x)\in(0,1)) for every (x\in U).

Restrict (H) to (U) for the lift on that piece, but retain (H) on (C) for the continuity/pasting argument. Repeat for (U(d_n)), using endpoints (c_n,e_n). This proves the needed local extension from the stated hypotheses; no additional perfect-normality assumption beyond metrizability of (C) is needed.

## 3. Infinite gluing: the missing diagonal detail

The paper's last continuity case has (s_k\to s\in A\cup B_0), with piece indices (n_k\) strictly increasing and (g(s_k)\in\{b_{n_k},d_{n_k}\}), while (g(s)=x\in w(X)).

Fix a path-connected open neighborhood (V) of (x). To invoke Lemma 4.5(3), one needs a sequence of endpoints in (\partial O_{n_k}) converging to (x); merely knowing that each (O_{n_k}) meets (V) does not by itself provide that sequence. The following diagonal completion supplies it and proves the required eventual containment.

Choose a decreasing countable neighborhood base (W_1\supseteq W_2\supseteq\cdots) of path-connected open neighborhoods of (x), with (W_j\subseteq V). This exists because (X) is metrizable and locally path-connected. By Lemma 5.2, each (q(W_j)) is open; it is also path-connected as the continuous image of (W_j). Since (g(s_k)\to x), for each fixed (j) all sufficiently large (k) satisfy (g(s_k)\in q(W_j)). The separation property used in the paper's proof then implies
[
W_j\cap\partial O_{n_k}\ne\varnothing
]
for all sufficiently large (k): a path in (q(W_j)) from (x) to (b_{n_k}) or (d_{n_k}) must meet the separating endpoint set, and (q) is the identity on the wild set.

Now suppose, for contradiction, that infinitely many (O_{n_k}) are not contained in (V). Restrict to that subsequence of indices. For each (j), choose a later index (k_j), strictly increasing with (j), and an endpoint
[
p_j\in W_j\cap\partial O_{n_{k_j}}.
]
Because the (W_j) form a decreasing neighborhood base, (p_j\to x). Lemma 4.5(3), applied to the strictly increasing indices (n_{k_j}) and endpoints (p_j), implies (O_{n_{k_j}}\subseteq V) for all sufficiently large (j). This contradicts the choice of the subsequence. Hence (O_{n_k}\subseteq V) for all but finitely many (k).

The corrected local extensions take (U(b_{n_k})) into (B_{n_k}\subset O_{n_k}) and (U(d_{n_k})) into (D_{n_k}\subset O_{n_k}). Therefore the lifted sequence is eventually in every path-connected open neighborhood (V) of (x), which proves convergence to (x=\widetilde g(s)).

For the other accumulation case (g(s)=c_m), (q(O_m)=\{b_m,c_m,d_m\}) is an open neighborhood of (c_m), so convergence forces the piece index to equal (m) eventually. The two closure extensions for that fixed (m) agree with (k) on their boundaries; their closed-domain pasting with the base map gives continuity. Sequences with indices bounded reduce to finitely many such closed-domain pieces; sequences with unbounded indices have a subsequence with strictly increasing indices, to which the preceding arguments apply. Since (B) is metrizable, sequential continuity suffices.

Thus the infinite-gluing argument has a short, valid completion from the paper's stated lemmas. The diagonal step is omitted in the printed proof as presented; it is not an obstruction once supplied.

## 4. Corollary 5.6

Conditional on Lemma 5.5, the corollary's deductions are standard and valid: the pairs ((I^{n+1},I^n\times\{0\})) give the disk homotopy lifting property, hence a Serre fibration; applying the lifting property to ((D^{n+1},S^n)) over a constant base point shows every fiber is weakly contractible (including path-connectedness from (n=0)); the homotopy exact sequence then gives isomorphisms on homotopy groups. Both spaces are path-connected.

## 5. Verification boundary

- Mathematical local repair: established on paper using Lemma 5.4 and the closed metrizable space (C=\overline U).
- Infinite-gluing completion: established above using Lemmas 4.5(3), 5.2, and the separation property explicitly invoked in the paper.
- Corollary 5.6: follows conditionally from the repaired Lemma 5.5 by standard Serre-fibration arguments.
- Lean verification: **failed**, not passed. GitHub Actions run [40991467393](https://github.com/inaciovasquez2020/urf-textbook/actions/runs/40991467393) failed compiling `CountablePeano/LocalExtension.lean`; errors include an unresolved `Decidable s.Nonempty`, unknown `Metric.continuous_infDist`, unsolved goals, and declarations containing `sorry`. The axiom audit was skipped. No formal verification receipt exists.

**Communication boundary:** It is appropriate to send a narrowly phrased proof-clarification email identifying the boundary/domain mismatch and asking whether the intended domain is \(\overline{U(b_n)}\). Do not claim the lemma or theorem is false. Do not describe the Lean scaffold as verified. The diagonal completion can be offered as a supplementary detail, not as an accusation of a fatal gap.
