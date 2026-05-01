# Transition-Shell Probe for the Finite-Capacity Spacetime-Deflection Package

## Status

Computable frontier probe.

This document records an executable test for a naive \(C^2\) transition shell from the local alpha-beta certificate to a flat exterior.

It does not claim a global matching theorem.

## Candidate tested

The local certificate is

\[
\alpha=e^{-2ar},
\qquad
\beta=e^{2ar},
\]

equivalently

\[
\Phi=-ar,
\qquad
\Lambda=ar.
\]

The probe tests a \(C^2\) smoothstep transition to a flat exterior:

\[
\Phi_{\mathrm{ext}}=0,
\qquad
\Lambda_{\mathrm{ext}}=0.
\]

## Energy-condition margins

The executable probe evaluates the five scalar margins

\[
\rho,
\qquad
\rho+p_r,
\qquad
\rho+p_t,
\qquad
\rho-p_r,
\qquad
\rho-p_t.
\]

## Result

The default smoothstep-to-flat transition is expected to fail at least one sampled margin.

This is not a failure of the local alpha-beta certificate.

It means the naive transition shell is not the Global Matching Lemma.

## Artifact

The probe writes:

\[
\texttt{artifacts/grf/transition\_shell\_probe.json}
\]

with:

- sampled minimum margin values,
- the radius at which each sampled minimum occurs,
- the candidate status,
- the boundary interpretation.

## Boundary

This is a numerical frontier probe.

This is not interval arithmetic.

It is not an impossibility theorem.

It is not a global-existence theorem.

## Next missing object

A transition ansatz with interval-certified nonnegative margins on the full transition shell.
