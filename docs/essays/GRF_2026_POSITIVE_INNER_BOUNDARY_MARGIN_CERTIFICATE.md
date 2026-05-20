# GRF Positive Inner-Boundary Margin Certificate

Status: `FRONTIER_OPEN_MARGIN_CERTIFICATE_INTERFACE`

## Obligation

This document isolates the first full-solve obligation:

\[
O1:\qquad \rho(r_1)-p_t(r_1)\ge \eta>0.
\]

Let

\[
f(r)=\rho(r)-p_t(r).
\]

The required object is

\[
f(r_1)\ge \eta>0.
\]

## Executable certificate rule

A numeric O1 certificate must provide:

\[
f(r_1),
\qquad
\eta.
\]

The certificate verifies only when

\[
\eta>0
\]

and

\[
f(r_1)-\eta\ge0.
\]

Equivalently,

\[
f(r_1)\ge\eta>0.
\]

## Expected input

The expected executable certificate input path is

\[
\texttt{artifacts/grf/positive\_inner\_boundary\_margin\_input.json}.
\]

The required input fields are:

```json
{
  "certificate_id": "O1_POSITIVE_INNER_BOUNDARY_MARGIN",
  "status": "VERIFIED",
  "rho_minus_pt_r1": 0.0,
  "eta": 0.0
}
The values above are placeholders only. A valid certificate requires concrete values with
η>0
and
ρ_minus_pt_r1≥η.
Interface result
If the executable input exists and passes the checker, then O1 is certified:
PositiveInnerBoundaryMargin(r 
1
​	
 ,η).
This feeds the first-cell positivity certificate and the full-solve certificate gate.
Boundary
This is a certificate interface only.
It does not prove:
that η exists,
a computation of ρ(r 
1
​	
 )−p 
t
​	
 (r 
1
​	
 ),
a first-cell positivity certificate,
a multi-cell interval certificate,
WEC/DEC closure,
a matching theorem,
a physical realization theorem,
GRF theorem-level closure.
