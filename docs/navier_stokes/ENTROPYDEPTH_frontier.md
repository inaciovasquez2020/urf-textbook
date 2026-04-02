# Complexity / Chronos / EntropyDepth Frontier

## Status
Open problem.

## Weakest Sufficient Missing Theorem
### Finite Local-Pattern Compression Lemma
Fix
\[
k\ge 2,\qquad \Delta\ge 3,\qquad r\ge 1.
\]
Then there exist
\[
R=R(k,\Delta,r),\qquad M=M(k,\Delta,r)<\infty
\]
such that for every bounded-degree graph
\[
G,\qquad \deg(G)\le \Delta,
\]
and every FO\(^k\)-definable radius-\(r\) refinement rule \(\mathcal F\), the output label of any vertex \(v\) depends only on one of at most \(M\) rooted radius-\(R\) local pattern classes.

Equivalently, there exists a map
\[
\Theta_{\mathcal F}:\mathcal T_{k,\Delta,R}\to \Lambda_{\mathcal F},
\qquad |\mathcal T_{k,\Delta,R}|\le M,
\]
such that
\[
\mathcal F(\xi)(v)=\Theta_{\mathcal F}\!\big(\operatorname{tp}^{R}_{k}(G,\xi,v)\big)
\]
for every configuration \(\xi\) and vertex \(v\).

## Entropy Consequence
Consequently, every one-step refinement factors through a finite alphabet of size at most \(M\), hence
\[
\Delta H_t \le \log_2 M.
\]

Therefore, for any hard family with residual entropy
\[
H_0(n)\ge c n,
\]
one obtains
\[
\operatorname{ED}(G_n)\ge \frac{c}{\log_2 M}\,n,
\]
and if
\[
H_0(n)\ge c n\log n,
\]
then
\[
\operatorname{ED}(G_n)\ge \frac{c}{\log_2 M}\,n\log n.
\]

## Minimal Reduction Chain
1. Define the rooted local type space
\[
\mathcal T_{k,\Delta,R}.
\]

2. Prove finiteness:
\[
|\mathcal T_{k,\Delta,R}|<\infty.
\]

3. Show every radius-\(r\) FO\(^k\) refinement factors through
\[
\operatorname{tp}^{R}_{k}.
\]

4. Deduce
\[
\Delta H_t\le \log_2 |\mathcal T_{k,\Delta,R}|.
\]

5. Insert the hard-family entropy lower bound.

## Conditional Closure Statement
Conditional on the Finite Local-Pattern Compression Lemma and a hard family with
\[
H_0(n)\ge c n\log n,
\]
the Chronos / EntropyDepth program yields
\[
\operatorname{ED}(G_n)\ge \Omega(n\log n).
\]
