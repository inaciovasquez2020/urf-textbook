# Explicit Local Alpha-Beta Pair for Finite-Capacity Outward Deflection

## Status

Conditional local realization certificate.

This document supplies an explicit bounded two-function pair \((\alpha,\beta)\) on a finite annulus satisfying:

- finite capacity,
- outward optical deflection,
- radial NEC,
- weak energy condition,
- dominant energy condition.

It does not claim global matching, asymptotic flatness, uniqueness, physical material construction, or full semiclassical stability.

## Metric ansatz

Use

\[
ds^2=-\alpha(r)dt^2+\beta(r)dr^2+r^2d\Omega^2,
\]

with

\[
\alpha(r)=e^{-2ar},
\qquad
\beta(r)=e^{2ar},
\qquad
a>0.
\]

Equivalently,

\[
\Phi(r)=\frac12\log\alpha(r)=-ar,
\qquad
\Lambda(r)=\frac12\log\beta(r)=ar.
\]

Work on a finite annulus

\[
\Omega=\{r_0\le r\le r_1\},
\qquad
0<r_0<r_1<\infty.
\]

## Finite-capacity bounds

Since \(\alpha,\beta\) are smooth and positive,

\[
0<e^{-2ar_1}\le \alpha(r)\le e^{-2ar_0}<\infty,
\]

\[
0<e^{2ar_0}\le \beta(r)\le e^{2ar_1}<\infty.
\]

Moreover,

\[
\nabla\log\alpha=-2a,
\qquad
\nabla^2\log\alpha=0,
\]

\[
\nabla\log\beta=2a,
\qquad
\nabla^2\log\beta=0.
\]

Thus

\[
\sup_\Omega
\left(
|\nabla\log\alpha|
+
|\nabla^2\log\alpha|
+
|\nabla\log\beta|
+
|\nabla^2\log\beta|
\right)
=
4a<\infty.
\]

## Outward deflection

The optical index is

\[
n(r)=\alpha(r)^{-1/2}=e^{ar}.
\]

Hence

\[
\partial_r n(r)=ae^{ar}>0.
\]

Therefore the optical-geodesic condition for outward deflection is satisfied.

Equivalently,

\[
\Phi'(r)=-a<0.
\]

## Stress-energy components

For the two-function static spherical metric,

\[
8\pi\rho
=
\frac{1-\beta^{-1}}{r^2}
+
\frac{\beta'}{\beta^2r},
\]

\[
8\pi p_r
=
-\frac{1-\beta^{-1}}{r^2}
+
\frac{2\Phi'}{\beta r},
\]

\[
8\pi p_t
=
\frac1\beta
\left(
\Phi''
+
(\Phi')^2
-
\frac{\Phi'\beta'}{2\beta}
+
\frac{\Phi'}{r}
-
\frac{\beta'}{2\beta r}
\right).
\]

Substitute

\[
\Phi'=-a,
\qquad
\Phi''=0,
\qquad
\frac{\beta'}{\beta}=2a.
\]

Let

\[
x=ar>0.
\]

Then

\[
8\pi r^2\rho
=
1-e^{-2x}+2xe^{-2x},
\]

\[
8\pi r^2p_r
=
-1+e^{-2x}-2xe^{-2x},
\]

and

\[
8\pi r^2p_t
=
2e^{-2x}(x^2-x).
\]

Thus

\[
p_r=-\rho.
\]

## Radial NEC

The radial NEC is

\[
\rho+p_r\ge0.
\]

Here,

\[
\rho+p_r=0.
\]

Thus the radial NEC is saturated.

Equivalently, the corrected radial NEC condition is

\[
\frac{\beta'}{\beta}+2\Phi'=0.
\]

## Weak energy condition

The weak energy condition requires

\[
\rho\ge0,
\qquad
\rho+p_r\ge0,
\qquad
\rho+p_t\ge0.
\]

First,

\[
8\pi r^2\rho
=
1-e^{-2x}(1-2x).
\]

Since

\[
e^{2x}\ge 1-2x
\]

for \(x>0\), one has

\[
\rho\ge0.
\]

Second,

\[
\rho+p_r=0.
\]

Third,

\[
8\pi r^2(\rho+p_t)
=
1-e^{-2x}(1-2x^2).
\]

Since

\[
e^{2x}\ge 1-2x^2
\]

for \(x>0\), one has

\[
\rho+p_t\ge0.
\]

Therefore the weak energy condition holds on \(\Omega\).

## Dominant energy condition

The dominant energy condition requires

\[
\rho\ge0,
\qquad
\rho\pm p_r\ge0,
\qquad
\rho\pm p_t\ge0.
\]

Since \(p_r=-\rho\),

\[
\rho+p_r=0,
\qquad
\rho-p_r=2\rho\ge0.
\]

It remains to check \(\rho\pm p_t\).

The \(+\) inequality was already shown:

\[
\rho+p_t\ge0.
\]

For the \(-\) inequality,

\[
8\pi r^2(\rho-p_t)
=
1-e^{-2x}(1-4x+2x^2).
\]

Equivalently, it is enough to show

\[
e^{2x}\ge 1-4x+2x^2.
\]

Define

\[
F(x)=e^{2x}-1+4x-2x^2.
\]

Then

\[
F(0)=0,
\]

\[
F'(x)=2e^{2x}+4-4x,
\]

and

\[
F''(x)=4e^{2x}-4.
\]

For \(0<x\le1\),

\[
F'(x)>0.
\]

For \(x\ge1\),

\[
F''(x)\ge0
\]

and

\[
F'(1)=2e^2>0.
\]

Thus

\[
F(x)\ge0
\]

for all \(x>0\). Hence

\[
\rho-p_t\ge0.
\]

Therefore the dominant energy condition holds on \(\Omega\).

## Result

**Explicit Local Alpha-Beta Pair Certificate.**

For any finite annulus

\[
\Omega=\{r_0\le r\le r_1\},
\qquad
0<r_0<r_1<\infty,
\]

and any \(a>0\), the pair

\[
\alpha(r)=e^{-2ar},
\qquad
\beta(r)=e^{2ar}
\]

defines a finite-capacity two-function metric satisfying outward optical deflection, the weak energy condition, and the dominant energy condition on \(\Omega\).

## Boundary

This is a local annular certificate.

It does not establish:

- global regularity at \(r=0\),
- asymptotic flatness,
- matching to an exterior solution,
- uniqueness,
- physical material realization,
- quantum stability,
- full semiclassical admissibility.

## Remaining object

The next missing object is a global matching lemma connecting this local finite-capacity annular pair to an exterior admissible spacetime while preserving the selected energy and stability conditions.
