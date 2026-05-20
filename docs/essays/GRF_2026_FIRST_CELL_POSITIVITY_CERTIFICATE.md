# GRF First-Cell Positivity Certificate

Status: `CONDITIONAL_FIRST_CELL_CERTIFICATE`

## Object

Let

\[
f(r)=\rho-p_t.
\]

Fix the first cell

\[
I=[r_1,r_1+\Delta r].
\]

Assume the boundary margin

\[
f(r_1)\ge \eta.
\]

Assume the derivative modulus bound

\[
\forall r\in I,\qquad |f'(r)|\le L_{\rm cell}.
\]

Assume the cell-width condition

\[
\eta-L_{\rm cell}\Delta r\ge0.
\]

Then

\[
\forall r\in I,\qquad f(r)\ge0.
\]

Equivalently,

\[
\forall r\in [r_1,r_1+\Delta r],
\qquad
\rho(r)-p_t(r)\ge0.
\]

## Proof skeleton

For any \(r\in I\), the mean-value estimate gives

\[
f(r)\ge f(r_1)-L_{\rm cell}|r-r_1|.
\]

Since

\[
|r-r_1|\le\Delta r,
\]

we get

\[
f(r)\ge \eta-L_{\rm cell}\Delta r.
\]

By the certificate condition,

\[
\eta-L_{\rm cell}\Delta r\ge0.
\]

Therefore

\[
f(r)\ge0
\]

throughout the first cell.

## Certificate schema

A first-cell positivity certificate consists of the tuple

\[
(r_1,\Delta r,\eta,L_{\rm cell})
\]

with

\[
\eta\ge0,
\qquad
L_{\rm cell}\ge0,
\qquad
\Delta r\ge0,
\qquad
\eta-L_{\rm cell}\Delta r\ge0.
\]

The certificate closes only the first-cell nonnegativity implication.

## Boundary

This is a conditional first-cell certificate only.

It does not prove:
- that \(\eta\) is positive,
- that the derivative data defining \(L_{\rm cell}\) exist,
- a multi-cell interval certificate,
- a global matching theorem,
- WEC/DEC closure,
- GRF theorem-level closure,
- a physical realization theorem.
