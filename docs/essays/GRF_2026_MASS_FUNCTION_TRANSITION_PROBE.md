# Mass-Function Transition Probe

## Status

Computable frontier probe.

This document replaces direct smoothstep interpolation of \((\Phi,\Lambda)\) with interpolation of the Misner-Sharp mass function \(m(r)\).

It does not claim a global matching theorem.

## Structural change

The previous Schwarzschild transition probe interpolated metric functions directly.

This probe uses the mass variable

\[
m(r)=\frac r2\left(1-e^{-2\Lambda(r)}\right).
\]

This makes the density condition transparent:

\[
m'(r)=4\pi r^2\rho(r).
\]

The probe then chooses \(\Phi'\) to saturate the radial NEC:

\[
p_r=-\rho.
\]

## Candidate class

The transition shell uses a \(C^2\) quintic interpolation for \(m(r)\), matching:

\[
m(r_1),\quad m'(r_1),\quad m''(r_1)
\]

from the local alpha-beta certificate to

\[
M,\quad 0,\quad 0
\]

at the Schwarzschild exterior radius \(R_{\mathrm{out}}\).

## Tested margins

The probe samples:

\[
\rho,
\qquad
\rho+p_r,
\qquad
\rho+p_t,
\qquad
\rho-p_r,
\qquad
\rho-p_t,
\qquad
m'.
\]

## Artifact

The probe writes:

\[
\texttt{artifacts/grf/mass\_function\_transition\_probe.json}
\]

## Boundary

This is a numerical frontier probe.

This is not interval arithmetic.

A sampled pass is not a theorem.

A sampled failure is not an impossibility theorem.

The next missing object remains an interval-certified mass-function transition ansatz.
