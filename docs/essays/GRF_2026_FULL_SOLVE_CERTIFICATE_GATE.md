# GRF Full-Solve Certificate Gate

Status: `FRONTIER_OPEN_FULL_CERTIFICATE_GATE`

## Gate

A full GRF transition-shell solve requires all eight obligations below.

### O1. Positive inner-boundary margin

Required object:

\[
\rho(r_1)-p_t(r_1)\ge \eta>0.
\]

Status: `MISSING_NUMERIC_OR_SYMBOLIC_CERTIFICATE`.

### O2. Actual derivative data

Required object:

\[
|m|\le M_0,\quad |m'|\le M_1,\quad |m''|\le M_2,
\]

\[
|\Phi'|\le P_1,\quad |\Phi''|\le P_2,\quad |\Phi'''|\le P_3.
\]

These bounds must produce a concrete \(L_{\rm cell}\).

Status: `MISSING_DERIVATIVE_BOUND_CERTIFICATE`.

### O3. First-cell numeric certificate

Required object:

\[
\eta-L_{\rm cell}\Delta r\ge0.
\]

Status: `MISSING_FIRST_CELL_NUMERIC_CERTIFICATE`.

### O4. Multi-cell propagation

Required object:

\[
\forall j,\qquad
\eta_j-L_j\Delta r_j\ge0,
\]

with cells covering the whole transition shell.

Status: `MISSING_MULTI_CELL_CERTIFICATE`.

### O5. All WEC/DEC components

Required object: verified certificates for every required WEC/DEC component, not only

\[
\rho-p_t\ge0.
\]

Status: `MISSING_COMPONENT_INVENTORY_CERTIFICATES`.

### O6. Matching theorem

Required object: inner region, transition shell, and outer region glue with the required regularity.

Status: `MISSING_MATCHING_CERTIFICATE`.

### O7. Physical realization

Required object: the chosen \(m(r)\), \(\Phi(r)\), shell width, and parameters define an admissible geometry/matter model.

Status: `MISSING_REALIZATION_CERTIFICATE`.

### O8. Formal verification

Required object: an executable certificate package.

The expected input path is

\[
\texttt{artifacts/grf/transition\_shell\_full\_certificate\_input.json}.
\]

Status: `MISSING_FINAL_EXECUTABLE_CERTIFICATE`.

## Closure rule

GRF theorem-level closure is forbidden unless every required obligation is marked `VERIFIED` and the executable certificate checker passes.

## Boundary

This is a certificate gate only.

It does not prove:
- a positive inner-boundary margin,
- derivative data construction,
- a first-cell numeric certificate,
- a multi-cell interval certificate,
- WEC/DEC closure,
- a matching theorem,
- a physical realization theorem,
- GRF theorem-level closure.
