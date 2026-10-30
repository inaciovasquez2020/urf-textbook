# Independent audit: Lemma 5.5 and Corollary 5.6

**Source:** Jeremy Brazas and Petar Pavešić, [Countable Models of One-Dimensional Peano Continua](https://arxiv.org/abs/2610.35875), arXiv:2610.35875, version 1.

**Repository status:** independent literature audit; not a URF theorem, not a result of the URF framework, and not a claim that the paper's theorem is false.

## Finding 1 — extension-domain mismatch in the printed proof

In the proof of Lemma 5.5, the endpoint map is defined on the ambient boundary
\[
D_n=\partial_B U(b_n),
\]
but the text describes an extension
\[
h_n:U(b_n)\to A_n
\]
whose restriction to \(\partial U(b_n)\) equals the boundary map. Since
\(U(b_n)\) is open in \(B\), its ambient boundary is generally outside
\(U(b_n)\). Thus the restriction as written is not defined.

This is a domain/notation defect in the proof presentation. It is not a
counterexample to Lemma 5.5.

### Closure-domain correction

Set
\[
C_n=\overline{U(b_n)}^{\,B},\qquad D_n=\partial_B U(b_n).
\]
Then \(D_n\) is closed in \(C_n\), and \(C_n\) is a closed metrizable
subspace of \(B\). Extend the endpoint map on \(D_n\) over \(C_n\) with
target the closed arc \(\overline{B_n}\). Restrict the extension to
\(U(b_n)\) to define the lift, and use its retained boundary values
when gluing to the map on \(A\cup B_0\). Apply the same construction to
\(U(d_n)\).

The required endpoint control is stronger than merely mapping into the
closed arc: every point of \(U(b_n)\) must map into the open arc \(B_n\).
The local lemma below supplies exactly this control.

## Local extension lemma — metric distance construction

Let \((C,d)\) be a metric space and let \(E,F\subseteq C\) be disjoint
closed subsets. Define
\[
\delta_E(x)=
\begin{cases}
\inf_{e\in E}d(x,e),&E\ne\varnothing,\\
1,&E=\varnothing,
\end{cases}
\qquad
\delta_F(x)=
\begin{cases}
\inf_{f\in F}d(x,f),&F\ne\varnothing,\\
1,&F=\varnothing.
\end{cases}
\]
Then
\[
H(x)=\frac{\delta_E(x)}{\delta_E(x)+\delta_F(x)}
\]
is continuous, takes values in \([0,1]\), and satisfies
\[
H^{-1}(\{0\})=E,\qquad H^{-1}(\{1\})=F.
\]
The denominator is strictly positive: if both distances vanished, closedness
would imply \(x\in E\cap F\), contradicting disjointness. The distance
functions are continuous; for a closed nonempty set, distance vanishes
exactly on that set. The empty-set convention handles all degenerate cases.

Thus \(H\) is strictly between zero and one off \(E\cup F\). Composing
with an arc parametrization gives a continuous extension to a closed arc
whose interior points map to the open arc. This avoids invoking perfect
normality as a black box for this particular endpoint-valued boundary map.

The Lean formalization is isolated in
formalization/countable-peano/CountablePeano/LocalExtension.lean.
It is a local metric lemma only; it does not formalize the Peano continuum,
the quotient, the global lifting construction, or the infinite gluing.

## Infinite-gluing audit

After the closure-domain correction, the gluing is compatible on every
boundary because each closure extension agrees there with the prescribed
base map. For continuity, use sequential continuity (the domain \(B\) is
metrizable).

For a sequence converging to a point in an open lifting piece, openness of
that piece reduces continuity to its local extension. At a point of the
closed base \(A\cup B_0\), a sequence whose piece indices remain in a
finite set has subsequences in one fixed closure, where the closure
extension is continuous. For a subsequence with indices escaping every
finite set, the two cases in the paper's proof apply:

* At a point mapping to \(c_m\), the open neighborhood \(q(O_m)\)
  eventually excludes all piece indices other than \(m\).
* At a point mapping to \(x\in w(X)\), openness of \(q\) and the
  path-connected-neighborhood separation property (Lemma 4.5(3)) force the
  corresponding neighborhoods \(O_{n_k}\) to lie eventually in any
  chosen path-connected open neighborhood of \(x\).

This verifies the intended sequential-gluing strategy conditional on the
paper's stated separation property. The Lean local lemma does not formalize
this global sequential argument.

## Corollary 5.6 — separate deduction

1. Apply Lemma 5.5 to
   \((B,A)=(I^{n+1},I^n\times\{0\})\). This gives the disk homotopy
   lifting property, hence the Serre fibration property.
2. For a fiber \(F_y=q^{-1}(y)\), apply Lemma 5.5 to
   \((D^{n+1},S^n)\), with the base map constantly \(y\). Every map
   \(S^n\to F_y\) extends over \(D^{n+1}\); for \(n=0\), this also
   gives path-connectedness. Thus each fiber is weakly contractible.
3. The homotopy exact sequence of a Serre fibration with nonempty weakly
   contractible fibers gives isomorphisms on all homotopy groups. Since
   both total and base spaces are path-connected, the map is a weak
   homotopy equivalence.

This deduction is conditional on Lemma 5.5. It does not independently
repair or prove the global lifting lemma.

## Verification status

- [x] Identify and record the closure-domain mismatch.
- [x] Give an explicit metric construction for the local endpoint-controlled extension.
- [x] Check the intended infinite-gluing argument against the corrected domains.
- [x] Separate the Serre-fibration and fiber deductions.
- [ ] Compile the Lean local lemma.
- [ ] Independently machine-check the corrected global gluing.
- [ ] Reassess the paper's theorem after the remaining obligations pass.

**Boundary:** no Lean build receipt is claimed until the isolated Mathlib project
builds successfully. No independent theorem-level closure is claimed.
