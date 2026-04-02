# Chronos Core

## Status
Open problem.

## Canonical Target
Construct a bounded-degree hard family
\[
\{G_n\}_{n\ge 1}
\]
and prove
\[
\operatorname{ED}(G_n)\ge \Omega(n\log n).
\]

## Weakest Sufficient Reduction
It suffices to establish the following three ingredients.

### 1. Finite Local-Pattern Compression
For fixed
\[
k\ge 2,\qquad \Delta\ge 3,\qquad r\ge 1,
\]
there exist
\[
R=R(k,\Delta,r),\qquad M=M(k,\Delta,r)<\infty
\]
such that every FO\(^k\)-definable radius-\(r\) refinement rule factors through the rooted local type map
\[
\operatorname{tp}^R_k.
\]

Hence every one-step refinement satisfies
\[
\Delta H_t \le \log_2 M.
\]

### 2. Hard-Family Residual Entropy
There exists a bounded-degree hard family \(\{G_n\}\) with
\[
H_0(n)\ge c\,n\log n
\]
for some constant \(c>0\).

### 3. Entropy-to-Depth Amplification
If
\[
\Delta H_t \le C
\]
for every step and
\[
H_0(n)\ge c\,n\log n,
\]
then
\[
\operatorname{ED}(G_n)\ge \frac{c}{C}\,n\log n.
\]

## Canonical Conditional Theorem
Conditional on the three ingredients above,
\[
\operatorname{ED}(G_n)\ge \Omega(n\log n).
\]

## Minimal Proof Order
1. Prove finite local-pattern compression.
2. Specify the bounded-degree hard family.
3. Prove the residual entropy lower bound.
4. Prove the entropy-to-depth amplification inequality.
5. Conclude the Chronos lower bound.

## Frontier Marker
The irreducible open object is:
\[
\text{Finite Local-Pattern Compression}
+
\text{Hard Family with } H_0(n)\ge c\,n\log n.
\]
