# Positive-Mass Schwarzschild Transition Probe

## Status

Computable frontier probe.

This document adds a sampled search probe for matching the local finite-capacity alpha-beta certificate to a positive-mass Schwarzschild exterior.

It does not claim a global matching theorem.

## Motivation

The flat-exterior obstruction shows that matching the local certificate to flat space is incompatible with WEC mass monotonicity.

The corrected exterior target is positive-mass Schwarzschild with

\[
M\ge m_{\mathrm{loc}}(r_1).
\]

## Probe

The executable probe searches over finite values of:

\[
M/m_{\mathrm{loc}}(r_1)
\]

and transition radii

\[
R_{\mathrm{out}}.
\]

For each candidate it samples the five margins

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

## Artifact

The probe writes:

\[
\texttt{artifacts/grf/schwarzschild\_transition\_probe.json}
\]

containing:

- candidate count,
- best sampled candidate,
- sampled minimum margin values,
- status,
- next missing object.

## Boundary

This is a numerical frontier probe.

This is not interval arithmetic.

A sampled pass is not a theorem.

A sampled failure is not an impossibility theorem.

The next missing object remains an interval-certified positive-mass Schwarzschild transition ansatz.
