# Global Matching Frontier for the Finite-Capacity Spacetime-Deflection Package

## Status

Frontier note.

This document isolates the next missing object after the explicit local alpha-beta pair.

It does not claim a global Einstein-matter construction theorem.

## Local certificate already available

On a finite annulus

\[
\Omega_{\mathrm{def}}=\{r_0\le r\le r_1\},
\qquad
0<r_0<r_1<\infty,
\]

the local certificate uses

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

This gives

\[
\Phi'(r)<0,
\]

finite capacity, outward optical deflection, radial NEC saturation, WEC, and DEC on the local annulus.

## Required global matching object

The next object is a smooth extension

\[
(\alpha,\beta):[r_0,\infty)\to(0,\infty)^2
\]

such that:

1. On the deflection annulus,

\[
\alpha=e^{-2ar},
\qquad
\beta=e^{2ar}.
\]

2. Outside a larger radius \(R_{\mathrm{out}}>r_1\), the metric becomes an admissible exterior, for example

\[
\alpha_{\mathrm{ext}}(r)=1-\frac{2M}{r},
\qquad
\beta_{\mathrm{ext}}(r)=\left(1-\frac{2M}{r}\right)^{-1},
\]

or another finite-capacity exterior satisfying the selected asymptotic condition.

3. The transition region is at least \(C^2\):

\[
\alpha,\beta\in C^2([r_0,\infty)).
\]

4. Positivity is preserved:

\[
0<\alpha_{\min}\le \alpha(r),
\qquad
0<\beta_{\min}\le \beta(r).
\]

5. Finite capacity is preserved:

\[
\sup
\left(
|\nabla\log\alpha|
+
|\nabla^2\log\alpha|
+
|\nabla\log\beta|
+
|\nabla^2\log\beta|
\right)
<\infty.
\]

6. The selected energy inequalities hold through the transition shell.

## Energy-condition functionals

Set

\[
\Phi=\frac12\log\alpha,
\qquad
\Lambda=\frac12\log\beta.
\]

For

\[
ds^2=-e^{2\Phi(r)}dt^2+e^{2\Lambda(r)}dr^2+r^2d\Omega^2,
\]

define

\[
8\pi\rho
=
\frac{1-e^{-2\Lambda}}{r^2}
+
\frac{2\Lambda'e^{-2\Lambda}}{r},
\]

\[
8\pi p_r
=
-\frac{1-e^{-2\Lambda}}{r^2}
+
\frac{2\Phi'e^{-2\Lambda}}{r},
\]

\[
8\pi p_t
=
e^{-2\Lambda}
\left(
\Phi''
+
(\Phi')^2
-
\Phi'\Lambda'
+
\frac{\Phi'-\Lambda'}{r}
\right).
\]

The global matching problem is to construct \(\Phi,\Lambda\) such that the following inequalities hold in the transition shell:

\[
\rho\ge0,
\]

\[
\rho+p_r\ge0,
\qquad
\rho+p_t\ge0,
\]

\[
\rho-p_r\ge0,
\qquad
\rho-p_t\ge0.
\]

## Smooth junction condition

A purely piecewise construction is not sufficient.

To avoid an artificial thin shell, the matching must preserve at least the no-jump condition for the induced geometry and extrinsic curvature.

A sufficient working condition is:

\[
\alpha,\beta\in C^2
\]

across the matching region.

This is stronger than the minimal Israel-junction condition and keeps the stress-energy functionals ordinary rather than distributional.

## Global Matching Lemma

**Global Matching Lemma.**

Given a local finite-capacity outward-deflection certificate

\[
\alpha=e^{-2ar},
\qquad
\beta=e^{2ar}
\]

on \([r_0,r_1]\), construct a \(C^2\), positive, finite-capacity extension \((\alpha,\beta)\) to \([r_0,\infty)\) such that:

\[
\Phi'<0
\]

on the intended deflection annulus,

the selected exterior condition holds for \(r\ge R_{\mathrm{out}}\), and

\[
\rho\ge0,\quad
\rho\pm p_r\ge0,\quad
\rho\pm p_t\ge0
\]

hold everywhere.

## Boundary

This document does not prove the Global Matching Lemma.

It only isolates the precise next frontier.

## Weakest constructive route

Use a compactly supported \(C^2\) transition function \(\eta(r)\) and set

\[
\Phi(r)=
(1-\eta(r))(-ar)+\eta(r)\Phi_{\mathrm{ext}}(r),
\]

\[
\Lambda(r)=
(1-\eta(r))(ar)+\eta(r)\Lambda_{\mathrm{ext}}(r).
\]

Then reduce the global problem to verifying the five scalar inequalities

\[
\rho\ge0,
\qquad
\rho+p_r\ge0,
\qquad
\rho+p_t\ge0,
\qquad
\rho-p_r\ge0,
\qquad
\rho-p_t\ge0
\]

on the compact transition interval.

## Next missing object

A computable transition-shell certificate:

\[
\eta,\Phi_{\mathrm{ext}},\Lambda_{\mathrm{ext}},r_1,R_{\mathrm{out}},a,M
\]

with interval-arithmetic verification of the five energy-condition inequalities.
