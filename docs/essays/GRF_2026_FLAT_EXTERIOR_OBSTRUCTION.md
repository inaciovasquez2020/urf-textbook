# Flat-Exterior Obstruction for the Finite-Capacity Transition Shell

## Status

Conditional structural obstruction.

This document explains why the naive smoothstep-to-flat transition-shell probe fails.

It does not prove global matching.

It identifies the correct replacement exterior.

## Setup

Use the static spherical metric

\[
ds^2=-e^{2\Phi(r)}dt^2+e^{2\Lambda(r)}dr^2+r^2d\Omega^2.
\]

Define the Misner-Sharp mass function

\[
m(r)=\frac r2\left(1-e^{-2\Lambda(r)}\right).
\]

Then

\[
m'(r)=4\pi r^2\rho(r).
\]

Therefore, under the weak energy condition

\[
\rho\ge0,
\]

the mass function is monotone nondecreasing:

\[
m'(r)\ge0.
\]

## Local certificate mass

The local alpha-beta certificate has

\[
\alpha=e^{-2ar},
\qquad
\beta=e^{2ar},
\]

so

\[
\Phi=-ar,
\qquad
\Lambda=ar.
\]

Hence

\[
m_{\mathrm{loc}}(r)
=
\frac r2\left(1-e^{-2ar}\right).
\]

For every

\[
a>0,
\qquad r>0,
\]

one has

\[
m_{\mathrm{loc}}(r)>0.
\]

In particular,

\[
m_{\mathrm{loc}}(r_1)
=
\frac {r_1}2\left(1-e^{-2ar_1}\right)
>0.
\]

## Flat exterior obstruction

A flat exterior has

\[
\Lambda_{\mathrm{flat}}=0,
\]

so

\[
m_{\mathrm{flat}}(r)=0.
\]

If a transition starts from the local certificate at \(r_1\), then

\[
m(r_1)>0.
\]

If it ends in a flat exterior, then eventually

\[
m(r)=0.
\]

Thus \(m\) must decrease somewhere.

But under \(\rho\ge0\),

\[
m'(r)=4\pi r^2\rho(r)\ge0.
\]

Therefore a WEC-preserving transition from the local alpha-beta certificate to a flat exterior cannot exist.

## Interpretation of the numerical probe

The transition-shell probe found negative sampled margins for the naive smoothstep-to-flat candidate.

This is structurally expected: the candidate attempts to reduce positive local mass to zero while preserving WEC/DEC margins.

The failure is not evidence against the local alpha-beta certificate.

It is evidence that flat exterior matching is the wrong target.

## Correct replacement exterior

The exterior target should be Schwarzschild-type with mass

\[
M\ge m_{\mathrm{loc}}(r_1).
\]

For Schwarzschild exterior,

\[
e^{2\Phi_{\mathrm{ext}}}=1-\frac{2M}{r},
\qquad
e^{2\Lambda_{\mathrm{ext}}}=
\left(1-\frac{2M}{r}\right)^{-1},
\]

and

\[
m_{\mathrm{ext}}(r)=M.
\]

This is compatible with monotone mass provided

\[
M\ge m_{\mathrm{loc}}(r_1).
\]

## Corrected next frontier

Replace:

\[
\text{local certificate} \to \text{flat exterior}
\]

with:

\[
\text{local certificate} \to \text{positive-mass Schwarzschild exterior}.
\]

## Boundary

This document proves only the flat-exterior obstruction under \(\rho\ge0\).

It does not construct the Schwarzschild matching shell.

It does not prove global existence.

It does not prove semiclassical stability.

## Next missing object

A computable positive-mass Schwarzschild transition-shell certificate satisfying:

\[
M\ge m_{\mathrm{loc}}(r_1),
\]

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

through the transition shell.
