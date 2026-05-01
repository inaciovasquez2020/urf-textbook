# Two-Function Frontier for Finite-Capacity Outward Deflection

## Structural replacement

Replace the one-function ansatz

\[
ds^2=-\alpha(r)dt^2+dr^2+r^2d\Omega^2
\]

by the two-function ansatz

\[
ds^2=-\alpha(r)dt^2+\beta(r)dr^2+r^2d\Omega^2,
\qquad
\alpha(r)>0,\quad \beta(r)>0.
\]

Set

\[
\Phi(r)=\frac12\log \alpha(r),
\qquad
\Lambda(r)=\frac12\log \beta(r).
\]

## Einstein-tensor components

For

\[
ds^2=-e^{2\Phi(r)}dt^2+e^{2\Lambda(r)}dr^2+r^2d\Omega^2,
\]

the mixed Einstein tensor satisfies

\[
G^t_t
=
-\left(
\frac{1-e^{-2\Lambda}}{r^2}
+
\frac{2\Lambda'e^{-2\Lambda}}{r}
\right),
\]

\[
G^r_r
=
-\frac{1-e^{-2\Lambda}}{r^2}
+
\frac{2\Phi'e^{-2\Lambda}}{r},
\]

\[
G^\theta_\theta
=
G^\phi_\phi
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

Equivalently, in terms of \(\beta=e^{2\Lambda}\),

\[
G^t_t
=
-\left(
\frac{1-\beta^{-1}}{r^2}
+
\frac{\beta'}{\beta^2 r}
\right),
\]

\[
G^r_r
=
-\frac{1-\beta^{-1}}{r^2}
+
\frac{2\Phi'}{\beta r},
\]

\[
G^\theta_\theta
=
G^\phi_\phi
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

## Matter variables

With

\[
T^\mu_{\ \nu}=\frac1{8\pi}G^\mu_{\ \nu},
\]

write

\[
T^\mu_{\ \nu}
=
\operatorname{diag}(-\rho,p_r,p_t,p_t).
\]

Then

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

## Outward-deflection condition

The optical index is

\[
n(r)=\alpha(r)^{-1/2}=e^{-\Phi(r)}.
\]

Outward deflection is enforced by

\[
\partial_r n(r)>0.
\]

Equivalently,

\[
\Phi'(r)<0.
\]

## Radial NEC condition

The radial null energy condition is

\[
\rho+p_r\ge0.
\]

Using the formulas above,

\[
8\pi(\rho+p_r)
=
\frac{\beta'}{\beta^2r}
+
\frac{2\Phi'}{\beta r}.
\]

Hence the radial NEC is equivalent to

\[
\frac{\beta'}{\beta}
+
2\beta\Phi'
\ge0.
\]

Since outward deflection gives \(\Phi'<0\), radial NEC requires

\[
\frac{\beta'}{\beta}
\ge
-2\beta\Phi'.
\]

## Weakest replacement lemma

**Two-Function Finite-Capacity Realization Lemma.**

Let \(\Omega=\{r_0\le r\le r_1\}\), \(0<r_0<r_1<\infty\).  
Let \(\alpha,\beta\in C^2(\Omega)\) satisfy

\[
0<\alpha_{\min}\le \alpha\le \alpha_{\max}<\infty,
\qquad
0<\beta_{\min}\le \beta\le \beta_{\max}<\infty,
\]

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
<\infty,
\]

\[
\Phi'(r)<0,
\]

and

\[
\frac{\beta'}{\beta}
+
2\beta\Phi'
\ge0.
\]

Then the two-function metric has finite-capacity outward deflection and satisfies the radial null energy condition.

## Remaining obstruction

The tangential NEC and dominant/weak energy conditions reduce to the remaining inequalities

\[
\rho+p_t\ge0,
\qquad
\rho\ge0,
\qquad
\rho\pm p_r\ge0,
\qquad
\rho\pm p_t\ge0.
\]

The next missing object is an explicit bounded pair \((\alpha,\beta)\) satisfying these inequalities while preserving \(\Phi'<0\).
