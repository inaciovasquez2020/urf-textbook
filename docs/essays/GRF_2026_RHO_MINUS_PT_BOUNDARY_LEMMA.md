# GRF 2026 — \(\rho-p_t\) Inner-Boundary Sign Lemma

## Status

`ANALYTIC_SIGN_LEMMA`

## Setup

Use the static spherical metric

\[
ds^2=-e^{2\Phi(r)}dt^2+\beta(r)\,dr^2+r^2d\Omega^2
\]

with Misner-Sharp relation

\[
\beta(r)=\frac{1}{1-2m(r)/r}.
\]

Then

\[
\frac{\beta'}{\beta}
=
\frac{2m'/r-2m/r^2}{1-2m/r}.
\]

## Tangential-pressure formula

In the normalization used by the GRF probes,

\[
\rho=\frac{m'}{r^2},
\]

and

\[
p_t
=
\beta^{-1}
\left[
\Phi''
+
(\Phi')^2
-
\frac{\beta'}{2\beta}\Phi'
+
\frac{\Phi'}{r}
-
\frac{\beta'}{2\beta r}
\right].
\]

Therefore

\[
\rho-p_t
=
\frac{m'}{r^2}
-
\beta^{-1}
\left[
\Phi''
+
(\Phi')^2
-
\frac{\beta'}{2\beta}\Phi'
+
\frac{\Phi'}{r}
-
\frac{\beta'}{2\beta r}
\right].
\]

## Inner-boundary inequality

At \(r=r_1\), write

\[
m_1=m(r_1),\quad
m_1'=m'(r_1),\quad
\Phi_1'=\Phi'(r_1),\quad
\Phi_1''=\Phi''(r_1).
\]

The analytic necessary boundary condition for the first interval cell is

\[
\frac{m_1'}{r_1^2}
\ge
\left(1-\frac{2m_1}{r_1}\right)
\left[
\Phi_1''
+
(\Phi_1')^2
+
\frac{\Phi_1'}{r_1}
\right]
-
\left(
\frac{m_1'}{r_1}
-
\frac{m_1}{r_1^2}
\right)
\left(
\Phi_1'
+
\frac{1}{r_1}
\right).
\]

Equivalently,

\[
(\rho-p_t)(r_1)\ge0.
\]

## Radial NEC saturation substitution

Under radial NEC saturation,

\[
\rho+p_r=0,
\]

the redshift derivative used by the probes is

\[
\Phi_1'
=
\beta_1\frac{m_1'}{r_1^2},
\qquad
\beta_1=\frac{1}{1-2m_1/r_1}.
\]

Thus any next ansatz must choose \(\Phi_1''\), or an equivalent second-order redshift-control parameter, so that the displayed inequality is satisfied before interval search.

## Boundary

This is an analytic sign lemma.

It is not a global matching theorem.

It is not a positive interval certificate.

It is not WEC/DEC closure.

It is not GRF theorem-level closure.

It is not a physical realization theorem.

## Next missing object

first-cell interval extension lemma for rho_minus_pt
