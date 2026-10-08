# Research Architecture: Finite Structural Verification

## Purpose

This note records a cross-project architectural pattern visible across the research repositories. It is an exposition and navigation artifact, not a claim that the projects compose into one theorem.

The recurring method is:

\[
\boxed{
\text{object}
\to
\text{representation}
\to
\text{local rule}
\to
\text{invariant / defect}
\to
\text{wall}
\to
\text{finite witness}
\to
\text{certified consequence}
}
\]

The central discipline is to expose the exact point where a desired global implication is not yet proved.

## 1. The common engine

A difficult global problem is first replaced by a representation in which the relevant information is finite, normalized, or mechanically checkable.

Then a local transition rule is studied.

An invariant, defect, separation quantity, or structural witness constrains what that transition can do.

When the desired progress does not occur, the failure is not hidden. It becomes an explicit wall:

\[
\text{progress}
\quad\lor\quad
\text{obstruction}.
\]

If the obstruction can continue indefinitely while the relevant state space is finite, recurrence follows:

\[
\text{infinite continuation}
+
\text{finite state space}
\Rightarrow
\text{repeated state}.
\]

Recurrence is then converted, where proved, into a more concrete structural witness. That witness may support a machine-checkable certificate, an independently verifiable artifact, or a precisely stated conditional frontier.

The final distinction is essential:

\[
\boxed{
\text{certified consequence}
\not\Rightarrow
\text{unconditional global theorem}
}
\]

unless the remaining bridge has itself been proved.

## 2. Project roles

### BEpTy — separation branch

The declared class uses a coarse representation

\[
J(X)=(FN(X),LSpan(X))
\]

together with a second valuation \(V_2(X)\).

The proved pattern is:

\[
J(X)=J(Y)
\land
V_2(X)\ne V_2(Y)
\Rightarrow
X\not\cong Y.
\]

This is the separation form of the general architecture: a shared coarse representation plus a distinguishing invariant yields a certified non-equivalence result within the declared scope.

### PachnerInvariant — local energy branch

The central quantity is

\[
\Theta(T,\lambda)
=
\sum_e(\deg_e-3)^2
+
\lambda\sum_v(\deg_v-6)^2.
\]

Local Pachner moves are analyzed against this quantity, with exact finite certification machinery.

The current conditional theorem surface is deliberately separated from the missing penalty inequalities. The architecture therefore reaches a certified local-move statement without silently promoting the conditional hypothesis to an unconditional theorem.

### Poincare-new-derivation — obstruction and recurrence branch

The program begins with

\[
\Phi(T)=\sum_v |d(v)-6|
\]

and local Pachner/Move32 structure.

When direct descent is unavailable, the formal development moves through increasingly concrete finite objects:

\[
\text{local fan structure}
\to
\text{finite edge state}
\to
\text{recurrence}
\to
\text{carrier reconstruction}
\to
\text{polygonal-loop certificate}
\to
\text{finite filling}.
\]

The current audited boundary is the final global implication from the filling data to a forced Pachner exit, strict descent, or contradiction. This note intentionally does not reopen that frontier.

### URF-core — verification infrastructure branch

URF-core supplies the common infrastructure for definitions, ledgers, theorem boundaries, certificates, and status discipline.

Its role is not to prove every project-specific theorem. Its role is to make claims auditable and prevent an executable artifact from being mistaken for a theorem that has not been discharged.

### chronos-urf-rr — executable structural branch

Chronos-URF-RR applies the same finite/executable philosophy to rigidity and recurrence-style structural constraints.

Its current frontier remains conditional where the analytic or structural bridge has not been proved.

### AKCL and cells-downwards-rh — quantitative separation branch

These projects express the same architecture in quantitative form:

\[
\text{structural wall}
\to
\text{separation / coercivity quantity}
\to
\text{certificate}.
\]

The key unresolved steps are explicit transfer or coercivity bridges rather than being hidden inside numerical output.

### clay-problem-lab — terminal-resonance branch

The Clay-facing work uses residuals, terminal configurations, and coercivity-style quantities to isolate the remaining resonance/curvature obstruction.

Its conditional status is part of the result surface; it is not promoted to a Clay closure claim.

### cslib-fmt — formal foundation branch

CSLIB-FMT supplies foundational formalized combinatorial infrastructure. Its role is to make lower-level objects and closure lemmas available to higher-level developments.

### YM and cosmology — executable artifact branches

The Yang–Mills and cosmology repositories demonstrate the same separation between construction and theorem closure:

\[
\text{implemented object}
\neq
\text{unconditional theorem}.
\]

The strongest claim is therefore attached to the executable, reproducible, and verifiable surface actually present.

## 3. The two main logical forms

Across the portfolio, two forms recur.

### Separation

\[
\boxed{
\Sigma(X)=\Sigma(Y)
\land
I(X)\ne I(Y)
\Rightarrow
X\not\sim Y
}
\]

This is the BEpTy-type branch.

### Progress or obstruction

\[
\boxed{
D(X)>0
\Rightarrow
\bigl(
\exists Y\sim X:\ D(Y)<D(X)
\bigr)
\lor
\operatorname{Wall}(X)
}
\]

The Poincare and Pachner developments are examples of this style, with project-specific definitions of \(D\), transitions, and walls.

A third operation then becomes available:

\[
\boxed{
\text{finite state}
+
\text{continued obstruction}
\Rightarrow
\text{recurrence}
}
\]

but recurrence becomes a contradiction only if an additional theorem establishes that the recurrent structure is impossible.

## 4. What is genuinely common

The following features are genuinely shared at the architectural level:

1. **Normalization or finite representation.**
2. **Explicit local transition rules.**
3. **An invariant, defect, valuation, or structural state.**
4. **A named obstruction or wall.**
5. **Finite-state or finite-witness reduction where available.**
6. **Machine-checkable or independently inspectable artifacts.**
7. **Explicit claim boundaries.**

These are methodological commonalities, not assertions that the mathematical theories are identical.

## 5. What must not be conflated

The following implications are not currently established merely because the projects share the architecture:

\[
\text{BEpTy separation}
\not\equiv
\text{Poincare descent},
\]

\[
\text{Pachner monotonicity}
\not\equiv
\text{global 3-manifold descent},
\]

\[
\text{URF certificate verification}
\not\equiv
\text{project-specific theorem proof},
\]

and

\[
\boxed{
\text{all project frontiers}
\not\Rightarrow
\text{one unconditional master theorem}.
}
\]

The portfolio should therefore be presented as a coherent methodology and collection of independently scoped results, not as a theorem-composition claim.

## 6. Master architectural statement

A concise description of the research program is:

\[
\boxed{
\mathsf{FINITE\ REPRESENTATION}
+
\mathsf{LOCAL\ LAW}
+
\mathsf{INVARIANT}
\Longrightarrow
\mathsf{STRUCTURAL\ WITNESS}
\Longrightarrow
\mathsf{CERTIFIED\ CONSEQUENCE}
}
\]

with the standing boundary:

\[
\boxed{
\mathsf{CERTIFIED\ CONSEQUENCE}
\not\Rightarrow
\mathsf{GLOBAL\ THEOREM}
}
\]

until the remaining global bridge is independently established.

This is the intended synthesis layer for readers moving between the individual repositories.

## 7. Status discipline

A project may therefore be:

- **closed** at its declared executable or formal scope;
- **conditional** when a named hypothesis remains;
- **open** when a specific bridge is missing;
- **artifact-complete** when a reproducible certificate exists even though the surrounding theorem remains open.

These labels describe different dimensions and should not be collapsed into a single percentage.

## Boundary

This document makes no claim of a unified proof of the mathematical problems represented by the portfolio. It records a common research architecture and the exact distinction between structural progress, certified artifacts, conditional bridges, and unresolved global implications.
