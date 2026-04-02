# IECP Frontier

## Open Status
IECP remains open.

## Exact Missing Lemma
A sufficient missing ingredient is the following local branching lemma.

### Local Branching Lemma
Let \(X\) be a metric phase space, \(\mathcal A\subset X\) forward-invariant, and \(\Phi_t\) the solution map. Fix \(r_0,\tau,\varepsilon_0>0\). There exist constants
\[
\kappa>1,\qquad c_0>0,\qquad C_0\ge 1
\]
such that for every \(u_0\in\mathcal A\), every \(t\ge 0\), and every spatial ball \(B\subset\Omega\) of radius \(r\le r_0\),
\[
\int_t^{t+\tau}\|\nabla \Phi_s(u_0)\|_{L^\infty}\,ds \ge \log \kappa
\]
implies the existence of sets
\[
E_1,\dots,E_M\subset B
\]
with
\[
M\ge e^{c_0},\qquad \operatorname{diam}(E_j)\le r/\kappa,\qquad \operatorname{dist}(E_i,E_j)\ge r/(C_0\kappa)\ \ (i\neq j),
\]
such that equal-size admissible perturbations \(\eta_i,\eta_j\) supported in \(E_i,E_j\) satisfy
\[
d_X\!\big(\Phi_\tau(u_0+\eta_i),\Phi_\tau(u_0+\eta_j)\big)\ge \varepsilon_0
\qquad (i\neq j).
\]

## Reduction
If the Local Branching Lemma holds and iterates stably on disjoint time windows, then IECP follows:
\[
\exists \alpha,\beta,\varepsilon_0,T_0>0
\]
such that
\[
\left(\int_0^T \|\nabla \Phi_t(u_0)\|_{L^\infty}\,dt \ge \alpha T\right)
\Longrightarrow
\log N_{\varepsilon_0}(\mathcal R(T;u_0))\ge \beta T
\]
for all \(T\ge T_0\).

## Minimal Proof Skeleton
1. Prove one-block branching.
2. Prove admissible perturbation persistence under iteration.
3. Prove multiplicative separation growth across blocks.
4. Convert multiplicative growth to linear covering entropy growth.

## Status Marker
Open problem.
