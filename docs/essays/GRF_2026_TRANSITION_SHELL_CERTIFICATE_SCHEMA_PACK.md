# GRF Transition-Shell Certificate Schema Pack

Status: `FRONTIER_OPEN_SCHEMA_PACK`

## Added objects

This pack adds the following frontier interfaces:

1. `CompleteGRFTransitionShellCertificate`
2. `O2_ACTUAL_DERIVATIVE_DATA`
3. `O4_MULTI_CELL_INTERVAL_PROPAGATION`
4. `O5_WEC_DEC_COMPONENT_INVENTORY`
5. `O6_MATCHING_THEOREM` / `O7_PHYSICAL_REALIZATION_THEOREM`

## Complete schema

A complete certificate requires:

\[
\mathrm{CompleteGRFTransitionShellCertificate}.
\]

The required gates are:

\[
O1,\ O2,\ O3,\ O4,\ O5,\ O6,\ O7,\ O8.
\]

GRF theorem-level closure is forbidden unless every required gate is `VERIFIED` by executable certificate data.

## O2 derivative-data interface

Required object:

\[
|m|\le M_0,\quad |m'|\le M_1,\quad |m''|\le M_2,
\]

\[
|\Phi'|\le P_1,\quad |\Phi''|\le P_2,\quad |\Phi'''|\le P_3.
\]

These must produce a concrete \(L_{\rm cell}\).

## O4 multi-cell interval interface

Required object:

\[
\forall j,\qquad \eta_j-L_j\Delta r_j\ge0.
\]

The cells must form a contiguous cover of the full transition shell.

## O5 WEC/DEC component inventory gate

Required components include:

\[
\rho\ge0,
\qquad
\rho+p_r\ge0,
\qquad
\rho+p_t\ge0,
\]

\[
\rho-|p_r|\ge0,
\qquad
\rho-|p_t|\ge0,
\qquad
\rho-p_t\ge0.
\]

Every listed component must have a verified interval certificate on the whole shell.

## O6/O7 matching-realization gate

Required objects:

\[
\text{inner-shell-outer matching with required regularity}
\]

and

\[
\text{admissible physical realization for the chosen shell data}.
\]

## Boundary

This is a schema/interface pack only.

It does not prove:
- eta existence,
- computation of \(\rho(r_1)-p_t(r_1)\),
- derivative data construction,
- a first-cell numeric certificate,
- a multi-cell interval certificate,
- WEC/DEC closure,
- a matching theorem,
- a physical realization theorem,
- GRF theorem-level closure.
