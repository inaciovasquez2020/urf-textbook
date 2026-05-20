# GRF First-Cell Derivative Modulus Bound

Status: `CONDITIONAL_DERIVATIVE_MODULUS_BOUND`

## Object

Let

\[
A(r)=1-\frac{2m(r)}{r},
\qquad
B(r)=\frac{r m'(r)-m(r)}{r^2 A(r)}.
\]

Use the standard transition-shell expression

\[
\rho-p_t
=
\frac{m'}{4\pi r^2}
-
\frac{A}{8\pi}
\left(
\Phi''
+(\Phi')^2
+\frac{\Phi'}{r}
-
B\left(\Phi'+\frac1r\right)
\right).
\]

Set

\[
Q
=
\Phi''
+(\Phi')^2
+\frac{\Phi'}{r}
-
B\left(\Phi'+\frac1r\right).
\]

Then

\[
(\rho-p_t)'
=
\frac1{4\pi}
\left(
\frac{m''}{r^2}
-
\frac{2m'}{r^3}
\right)
-
\frac1{8\pi}
\left(A'Q+AQ'\right),
\]

where

\[
A'=-\frac{2m'}r+\frac{2m}{r^2},
\]

\[
B'
=
\frac{(r m'')(r^2A)-(r m'-m)(2r-2m-2rm')}{(r^2A)^2},
\]

and

\[
Q'
=
\Phi'''
+2\Phi'\Phi''
+\frac{\Phi''}{r}
-\frac{\Phi'}{r^2}
-
B'\left(\Phi'+\frac1r\right)
-
B\left(\Phi''-\frac1{r^2}\right).
\]

## Conditional bound

Fix a first cell

\[
I=[r_1,r_1+\Delta r].
\]

Assume first-cell derivative data

\[
r\ge r_0>0,
\qquad
A(r)\ge a>0,
\]

and

\[
|m|\le M_0,\quad
|m'|\le M_1,\quad
|m''|\le M_2,
\]

\[
|\Phi'|\le P_1,\quad
|\Phi''|\le P_2,\quad
|\Phi'''|\le P_3
\]

on \(I\). Let

\[
R=r_1+\Delta r,
\]

\[
A_{\max}=1+\frac{2M_0}{r_0},
\qquad
A_1=\frac{2M_1}{r_0}+\frac{2M_0}{r_0^2},
\]

\[
N_{\max}=RM_1+M_0,
\qquad
D_1=2R+2M_0+2RM_1,
\]

\[
B_{\max}
=
\frac{N_{\max}}{r_0^2a},
\]

\[
B_1
=
\frac{(RM_2)(R^2A_{\max})+N_{\max}D_1}{r_0^4a^2}.
\]

Define

\[
Q_{\max}
=
P_2+P_1^2+\frac{P_1}{r_0}
+
B_{\max}\left(P_1+\frac1{r_0}\right),
\]

\[
Q_1
=
P_3+2P_1P_2+\frac{P_2}{r_0}+\frac{P_1}{r_0^2}
+
B_1\left(P_1+\frac1{r_0}\right)
+
B_{\max}\left(P_2+\frac1{r_0^2}\right).
\]

Then the first-cell derivative modulus is

\[
L_{\rm cell}
=
\frac1{4\pi}
\left(
\frac{M_2}{r_0^2}
+
\frac{2M_1}{r_0^3}
\right)
+
\frac1{8\pi}
\left(
A_1Q_{\max}+A_{\max}Q_1
\right).
\]

Hence

\[
\forall r\in I,\qquad
\left|
\frac{d}{dr}(\rho-p_t)(r)
\right|
\le
L_{\rm cell}.
\]

## Interface closure

This supplies the missing object required by the first-cell interval extension lemma:

\[
\mathrm{FirstCellDerivativeModulusBound}
(\rho-p_t,r_1,\Delta r,L_{\rm cell}).
\]

Consequently, if the previous boundary lemma supplies

\[
(\rho-p_t)(r_1)\ge \eta
\]

and

\[
\eta-L_{\rm cell}\Delta r\ge0,
\]

then

\[
\rho-p_t\ge0
\]

on the first cell.

## Boundary

This is a conditional derivative modulus only.

It does not prove:
- existence of the first-cell derivative data,
- a positive interval certificate,
- a global matching theorem,
- WEC/DEC closure,
- GRF theorem-level closure,
- a physical realization theorem.
