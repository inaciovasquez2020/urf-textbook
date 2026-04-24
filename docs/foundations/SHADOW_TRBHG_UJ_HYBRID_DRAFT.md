# Shadow–TRBHG–UJ Hybrid Classifier

## Status

Draft.

Conditional.

This note is a conservative classifier, not a claim of:
- unknown-sector existence;
- non-human origin;
- artificial metric engineering;
- traversable wormhole construction;
- faster-than-light transport;
- new spacetime physics from finite anomaly data.

## Inputs

### Input 1: Shadow of Infinity

A finite observable boundary trace may point toward a limiting or infinite regime without realizing that regime.

\[
\operatorname{Shadow}(X)
\neq
X.
\]

### Input 2: TRBHG

A time-reversed black-hole geometry is treated only as a causal-orientation template.

\[
\Theta(\mathcal M,g,\tau,\mathscr I^-,\mathscr I^+)
=
(\mathcal M,g,-\tau,\mathscr I^+,\mathscr I^-).
\]

### Input 3: UJ Unknown-Sector Classifier

Finite nondetection produces bounds.

It does not produce existence.

\[
\neg \operatorname{Detect}(X)
\not\Rightarrow
\exists X.
\]

## Hybrid Object

Let

\[
\mathcal O=(D,\Sigma,\varepsilon,A,\tau)
\]

where:

\[
D=\text{data},
\quad
\Sigma=\text{sensor system},
\quad
\varepsilon=\text{uncertainty model},
\quad
A=\text{admissibility constraints},
\quad
\tau=\text{causal orientation}.
\]

Define

\[
\mathsf H(\mathcal O)
=
\mathsf C_{\mathrm{UJ}}
\left(
\operatorname{Shadow}_{\tau}(\mathcal O),
\Theta,
A,
\varepsilon
\right).
\]

## Boundary Rule

A finite record may justify a boundary classification:

\[
\mathcal O
\leadsto
\operatorname{Shadow}_{\tau}(\mathcal O).
\]

It may not justify an ontological upgrade without an additional witness:

\[
\operatorname{Shadow}_{\tau}(\mathcal O)
\not\Rightarrow
\exists X_{\mathrm{unknown}}.
\]

## Time-Reversal Shadow Rule

For a future null boundary,

\[
\operatorname{Shadow}_{\tau}(\mathscr I^+)
=
\partial J^-_{\tau}(\mathscr I^+).
\]

For the reversed orientation,

\[
\operatorname{Shadow}_{-\tau}(\mathscr I^-)
=
\partial J^-_{-\tau}(\mathscr I^-)
=
\partial J^+_{\tau}(\mathscr I^-).
\]

Therefore,

\[
\Theta
\bigl(
\operatorname{Shadow}_{\tau}(\mathscr I^+)
\bigr)
=
\operatorname{Shadow}_{-\tau}(\mathscr I^-).
\]

## Classifier Guard

For every finite record \(\mathcal O\),

\[
\mathsf H(\mathcal O)
\notin
\{
\mathrm{CONFIRMED\_UNKNOWN\_SECTOR},
\mathrm{CONFIRMED\_NON\_HUMAN\_ORIGIN},
\mathrm{CONFIRMED\_METRIC\_ENGINEERING},
\mathrm{CONFIRMED\_TRAVERSABLE\_WORMHOLE}
\}
\]

unless an independent constructive witness is supplied.

## Allowed Outputs

\[
\mathsf H(\mathcal O)
\in
\{
\mathrm{MUNDANE},
\mathrm{SENSOR\_ARTIFACT},
\mathrm{ENVIRONMENTAL\_ARTIFACT},
\mathrm{AIR\_DOMAIN\_ADMISSIBLE},
\mathrm{NON\_AIR\_CANDIDATE},
\mathrm{UNKNOWN\_SECTOR\_BOUND\_ONLY},
\mathrm{METRIC\_TOPOLOGY\_CANDIDATE},
\mathrm{TIME\_REVERSAL\_SHADOW\_TEMPLATE},
\mathrm{INSUFFICIENT\_DATA}
\}.
\]

## Weakest Sufficient Upgrade Rule

An observation may be upgraded from

\[
\mathrm{UNKNOWN\_SECTOR\_BOUND\_ONLY}
\]

to

\[
\mathrm{NON\_AIR\_CANDIDATE}
\]

only if it supplies:

\[
\mathrm{calibrated\ multisensor\ coherence}
+
\mathrm{trajectory\ reconstruction}
+
\mathrm{artifact\ exclusion}
+
\mathrm{environmental\ exclusion}.
\]

It may be upgraded to

\[
\mathrm{METRIC\_TOPOLOGY\_CANDIDATE}
\]

only if it additionally supplies:

\[
\mathrm{causal\ anomaly}
+
\mathrm{conservation\ closure}
+
\mathrm{repeatability}
+
\mathrm{independent\ instrumentation}.
\]

## Minimal Missing Lemma

For finite observation records,

\[
\operatorname{Shadow}_{\tau}(\mathcal O)
+
\Theta
+
\neg \operatorname{Detect}
\]

does not imply

\[
\exists X_{\mathrm{unknown}}.
\]

## Executable Numerical Probe

The numerical probe is not evidence for an unknown sector.

It tests only the guard logic:

\[
\mathrm{nondetection}
\mapsto
\mathrm{UNKNOWN\_SECTOR\_BOUND\_ONLY}.
\]

\[
\min(
s_{\mathrm{sensor}},
s_{\mathrm{trajectory}},
s_{\mathrm{artifact\ exclusion}},
s_{\mathrm{environmental\ exclusion}}
)
\ge 0.80
\Rightarrow
\mathrm{NON\_AIR\_CANDIDATE}.
\]

\[
\min(
s_{\mathrm{nonair}},
s_{\mathrm{causal}},
s_{\mathrm{conservation}},
s_{\mathrm{repeatability}},
s_{\mathrm{independent}}
)
\ge 0.85
\Rightarrow
\mathrm{METRIC\_TOPOLOGY\_CANDIDATE}.
\]

It is implemented by:

\[
\texttt{tools/shadow\_trbhg\_uj\_numeric.py}
\]

and guarded by:

\[
\texttt{tests/test\_shadow\_trbhg\_uj\_numeric.py}.
\]

## Cosmological Boundary Probe

The cosmology numerical probe is not evidence for an unknown sector.

It tests whether a finite boundary-scale value behaves as a shadow value rather than an existence claim.

For rest wavelength \(\lambda_0\) and observed wavelength \(\lambda_{\mathrm{obs}}\),

\[
z
=
\frac{\lambda_{\mathrm{obs}}}{\lambda_0}
-
1.
\]

The low-\(z\) Hubble proxy is

\[
v
=
cz,
\qquad
d
=
\frac{cz}{H_0}.
\]

The finite shadow score is

\[
s_{\mathrm{cosmo}}
=
\frac{z}{1+z}.
\]

For the locked numerical case,

\[
\lambda_{\mathrm{obs}}=984.42\mathrm{nm},
\qquad
\lambda_0=656.28\mathrm{nm},
\]

so

\[
z=0.5,
\qquad
s_{\mathrm{cosmo}}=\frac13.
\]

The classifier must preserve:

\[
s_{\mathrm{cosmo}}=\frac13
\not\Rightarrow
\exists X_{\mathrm{unknown}}.
\]

It is guarded by:

\[
\texttt{tests/test\_shadow\_trbhg\_uj\_cosmology\_numeric.py}.
\]

## Repository Placement

Do not index this draft until one of the following is true:

\[
\text{Either}
\quad
\mathsf H
\text{ is needed by another note,}
\]

or

\[
\text{the hybrid produces a strictly new guard not already present in the three source notes.}
\]

## Decision Criterion

Add permanently only if this file contributes a new invariant:

\[
\mathrm{finite\ boundary\ trace}
\neq
\mathrm{existence\ claim}
\]

under simultaneous:

\[
\text{shadow interpretation}
+
\text{causal reversal template}
+
\text{unknown-sector nondetection guard}.
\]
