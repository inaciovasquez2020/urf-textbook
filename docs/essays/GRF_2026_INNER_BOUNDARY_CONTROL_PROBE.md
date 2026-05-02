# GRF 2026 — Inner-Boundary Control Probe

## Object

This note records an interval arithmetic probe targeting the inner-boundary tangential-pressure obstruction.

The obstruction identified by the previous interval probes is localized at the first transition cell.

The targeted margin is:

\[
\rho-p_t.
\]

## Ansatz

The transition is a quintic Hermite mass-function ansatz with explicit inner-boundary derivative and second-derivative control:

\[
m(r)=H_5(s),
\qquad
s=\frac{r-r_1}{R-r_1}.
\]

The controlled data are:

\[
m(r_1),\quad m'(r_1),\quad m''(r_1),
\quad
m(R),\quad m'(R),\quad m''(R).
\]

The redshift derivative is chosen by radial NEC saturation.

## Boundary

This is an interval arithmetic frontier probe.

It is not a theorem of global existence.

It is not an impossibility theorem.

It does not promote sampled numerical evidence to proof.

It only certifies the encoded finite interval partition and ansatz family.

## Next missing object

inner-boundary tangential-pressure control with certified nonnegative rho_minus_pt and all WEC/DEC margins
