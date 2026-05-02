# GRF 2026 — Interval Mass-Function Transition Probe

## Object

This note records an interval arithmetic frontier probe for the positive-mass mass-function transition problem.

The ansatz family is:

\[
m(r)=m_1+(M-m_1)q\!\left(\frac{r-r_1}{R-r_1}\right),
\]

where \(q\) is the \(C^2\) quintic smoothstep.

The metric coefficient is encoded through the Misner-Sharp relation:

\[
\beta(r)=\frac{1}{1-2m(r)/r}.
\]

The redshift derivative is chosen by radial NEC saturation.

## Certified margins

The generated artifact records interval lower bounds for:

- \(m'\)
- \(\rho\)
- \(\rho-p_r\)
- \(\rho-p_t\)
- \(\rho+p_r\)
- \(\rho+p_t\)

## Boundary

This is an interval arithmetic frontier probe.

It is not a theorem of global existence.

It is not an impossibility theorem.

It does not promote sampled numerical evidence to proof.

It only certifies the encoded finite interval partition and ansatz family.

## Current result

The current artifact status is either `CERTIFIED_PASS` or `FRONTIER_OPEN`.

`FRONTIER_OPEN` means the encoded interval family did not produce a certified positive lower bound.

## Next missing object

certified positive lower bound or replacement ansatz with interval certificate
