# GRF 2026 — First-Cell Interval Extension Lemma

## Status

`CONDITIONAL_INTERVAL_EXTENSION_LEMMA`

## Target

The remaining obstruction is the first-cell interval lower bound for

\[
\rho-p_t.
\]

The target cell is

\[
I_1=[r_1,r_1+\Delta r].
\]

## Conditional lemma

Let

\[
f(r)=\rho(r)-p_t(r).
\]

Assume:

\[
f(r_1)\ge \eta
\]

and

\[
|f'(r)|\le L
\qquad
\text{for all }r\in[r_1,r_1+\Delta r].
\]

If

\[
\eta-L\Delta r\ge0,
\]

then

\[
\inf_{r\in[r_1,r_1+\Delta r]} f(r)\ge0.
\]

Equivalently,

\[
\inf_{r\in[r_1,r_1+\Delta r]}(\rho-p_t)(r)\ge0.
\]

## Proof

For \(r\in[r_1,r_1+\Delta r]\), the mean-value inequality gives

\[
f(r)\ge f(r_1)-L|r-r_1|.
\]

Since \(|r-r_1|\le\Delta r\),

\[
f(r)\ge\eta-L\Delta r.
\]

Thus, if \(\eta-L\Delta r\ge0\),

\[
f(r)\ge0
\]

throughout the first cell.

## Frontier use

The next interval ansatz must provide:

\[
\eta=(\rho-p_t)(r_1)>0
\]

and a certified derivative-modulus bound

\[
|(\rho-p_t)'(r)|\le L
\]

on the first cell.

## Boundary

This is a conditional interval extension lemma.

It is not an existence proof for the derivative-modulus bound.

It is not a positive interval certificate.

It is not a global matching theorem.

It is not WEC/DEC closure.

It is not GRF theorem-level closure.

It is not a physical realization theorem.

## Next missing object

explicit derivative-modulus bound for rho_minus_pt on the first cell
