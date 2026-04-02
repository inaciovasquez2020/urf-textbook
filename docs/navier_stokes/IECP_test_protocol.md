# IECP Test Protocol

## Title
Irreducible Eulerian Complexity Production: Statement, Conditional Reduction, and Finite-Data Test

## Core Hypothesis
Let \(X\) be a metric phase space with metric \(d_X\), let \(\mathcal A \subset X\) be forward-invariant, let \(\Phi_t : \mathcal A \to X\) be the evolution map, and define the reachable set
\[
\mathcal R(T;u_0):=\{\Phi_T(v_0): v_0 \in \mathcal U(u_0)\},
\]
where \(\mathcal U(u_0)\subset \mathcal A\) is an admissible perturbation class around \(u_0\).

Define
\[
N_\varepsilon(\mathcal R(T;u_0))
\]
to be the minimal number of \(d_X\)-balls of radius \(\varepsilon\) needed to cover \(\mathcal R(T;u_0)\).

The IECP hypothesis is:
\[
\exists \alpha,\beta,\varepsilon_0,T_0>0\ \forall T\ge T_0\ \forall u_0\in\mathcal A:
\left(\int_0^T \|\nabla \Phi_t(u_0)\|_{L^\infty}\,dt \ge \alpha T\right)
\Longrightarrow
\log N_{\varepsilon_0}(\mathcal R(T;u_0)) \ge \beta T.
\]

## Conditional Local-to-Global Criterion
Assume there exist constants
\[
r_0>0,\quad \tau>0,\quad \kappa>1,\quad c_0>0,\quad C_0\ge 1,\quad \varepsilon_0>0
\]
such that for every \(u_0\in\mathcal A\), every \(t\ge 0\), and every ball \(B\subset\Omega\) of radius \(r\le r_0\),
\[
\int_t^{t+\tau}\|\nabla \Phi_s(u_0)\|_{L^\infty}\,ds \ge \log\kappa
\]
implies the existence of sets
\[
E_1,\dots,E_M\subset B
\]
with
\[
M\ge e^{c_0},\qquad \operatorname{diam}(E_j)\le r/\kappa,\qquad \operatorname{dist}(E_i,E_j)\ge r/(C_0\kappa)\ \ (i\neq j),
\]
such that admissible equal-size perturbations \(\eta_i,\eta_j\) supported in \(E_i,E_j\) satisfy
\[
d_X\!\big(\Phi_\tau(u_0+\eta_i),\Phi_\tau(u_0+\eta_j)\big)\ge \varepsilon_0
\qquad (i\neq j).
\]

Then there exist \(\alpha,\beta>0\) such that
\[
\int_0^T \|\nabla \Phi_t(u_0)\|_{L^\infty}\,dt \ge \alpha T
\Longrightarrow
\log N_{\varepsilon_0}(\mathcal R(T;u_0))\ge \beta T
\]
for all \(T\ge \tau\).

## Observable Quantities
For each trajectory \(u(t)=\Phi_t(u_0)\), define
\[
C(T;u_0):=\int_0^T \|\nabla u(\cdot,t)\|_{L^\infty}\,dt
\]
and
\[
K_\varepsilon(T;u_0):=\log N_\varepsilon(\mathcal R(T;u_0)).
\]

## Verification Test
A sufficient verification test for IECP on \((X,\mathcal A,\Phi_t)\) is:
\[
\exists \varepsilon_*,\alpha,\beta,T_0>0\ \forall T\ge T_0:
\quad
\inf_{\substack{u_0\in\mathcal A\\ C(T;u_0)\ge \alpha T}}
K_{\varepsilon_*}(T;u_0)\ge \beta T.
\]

## Falsification Test
A sufficient falsification test is:
\[
\exists \varepsilon_*>0,\ \exists \alpha>0,\ \exists T_n\to\infty,\ \exists u_{0,n}\in\mathcal A
\]
such that
\[
C(T_n;u_{0,n})\ge \alpha T_n
\]
for all \(n\), but
\[
\limsup_{n\to\infty}\frac{K_{\varepsilon_*}(T_n;u_{0,n})}{T_n}=0.
\]

## Finite-Data Discrete Protocol
Fix \(\Delta t>0\), \(T=M\Delta t\), and define
\[
t_m:=m\Delta t,\qquad
C^{\Delta t}(T;u_0):=\sum_{m=0}^{M-1}\Delta t\,\|\nabla u(\cdot,t_m)\|_{L^\infty}.
\]

Given terminal states
\[
u^{(1)}(T),\dots,u^{(N)}(T)\in X,
\]
define the separation graph
\[
G_{ij}:=\mathbf 1_{\{d_X(u^{(i)}(T),u^{(j)}(T))>\varepsilon\}}.
\]

If \(S\subset\{1,\dots,N\}\) is pairwise \(\varepsilon\)-separated, then
\[
K_\varepsilon(T)\ge \log |S|.
\]

Therefore the finite-data certification rule is:
\[
C^{\Delta t}(T;u_0)\ge \alpha T
\quad\text{and}\quad
\exists S \text{ pairwise }\varepsilon\text{-separated with } |S|\ge e^{\beta T}
\]
which implies
\[
K_\varepsilon(T;u_0)\ge \beta T.
\]

## Finite-Data Failure Rule
If there exist \(T_n\to\infty\) and samples at times \(T_n\) such that
\[
C^{\Delta t_n}(T_n;u_{0,n})\ge \alpha T_n
\]
but every pairwise \(\varepsilon_*\)-separated subset \(S_n\) of the sampled terminal states satisfies
\[
\log |S_n| = o(T_n),
\]
then the sampled data are inconsistent with IECP at scale \(\varepsilon_*\).

## Required Structural Inputs
1. A specified phase space \(X\) and metric \(d_X\).
2. A specified admissible perturbation class \(\mathcal U(u_0)\).
3. A specified terminal-state sampling rule.
4. A certified estimator or bound for \(\|\nabla u(\cdot,t)\|_{L^\infty}\).
5. A certified lower bound on maximal pairwise \(\varepsilon\)-separated subsets of sampled terminal states.

## Minimal Research Program
### Step 1
Prove a local branching lemma:
\[
\int_t^{t+\tau}\|\nabla u(\cdot,s)\|_{L^\infty}\,ds \ge \log\kappa
\Longrightarrow
\text{at least } e^{c_0}\text{ distinguishable descendants over time }\tau.
\]

### Step 2
Iterate the branching lemma over disjoint time blocks:
\[
[0,\tau], [\tau,2\tau], \dots, [(m-1)\tau,m\tau].
\]

### Step 3
Obtain multiplicative growth:
\[
N_{\varepsilon_0}(\mathcal R(m\tau;u_0))\ge e^{c_0 m}.
\]

### Step 4
Convert to linear growth:
\[
\log N_{\varepsilon_0}(\mathcal R(T;u_0))\ge \frac{c_0}{\tau}T - O(1).
\]

### Step 5
Deduce IECP with
\[
\beta=\frac{c_0}{2\tau}
\]
for \(T\) sufficiently large.

## Canonical Conditional Theorem
Conditional on the local branching lemma and its stable iteration under admissible perturbations,
\[
\exists \alpha,\beta,\varepsilon_0,T_0>0
\]
such that
\[
\forall T\ge T_0,\ \forall u_0\in\mathcal A,\qquad
\left(\int_0^T \|\nabla \Phi_t(u_0)\|_{L^\infty}\,dt \ge \alpha T\right)
\Longrightarrow
\log N_{\varepsilon_0}(\mathcal R(T;u_0))\ge \beta T.
\]

## Status
Open problem.
