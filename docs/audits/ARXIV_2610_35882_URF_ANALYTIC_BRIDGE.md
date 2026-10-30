# URF Analytic Bridge: arXiv:2610.35882

**Date:** 2026-10-30  
**External paper:** Chenye Zhang, *A Counterexample to a Bourgain–Brezis Sum-Space Estimate*, arXiv:2610.35882v1 (4 September 2026).  
**Purpose:** Test whether current URF formal vocabulary can represent and independently evaluate the paper's theorem. This note records the mathematical bridge and the formalization boundary; it does not claim an independent proof.

## 1. Paper claim under test

For every N >= 2 and integer K >= 16, the paper constructs a smooth, real-valued, mean-zero function Phi_K on T^N such that, with constants independent of N and K,

||grad Phi_K||_(H^-1/2 + L1) <= C,
||Phi_K||_(H^1/2 + W^1,1) >= c K^(1/4) - C.

This disproves the proposed uniform estimate from the ambient vector-field sum norm to the scalar sum norm. It does not disprove the nonlinear phase estimate discussed in the paper; the paper explicitly distinguishes those claims.

## 2. Exact analytic bridge: ambient versus gradient-constrained K-functionals

Use the inhomogeneous Sobolev norms and normalized Haar measure on the torus, as specified in the paper.

Let
X0 = H^-1/2(T^N; R^N), X1 = L1(T^N; R^N).
Let H^1/2_0 and W^1,1_0 denote mean-zero scalar functions, and define
G0 = {grad h : h in H^1/2_0} subset X0,
G1 = {grad w : w in W^1,1_0} subset X1,
with norms inherited from X0 and X1.

For a compatible pair (X0,X1), define
K(1,F;X0,X1) = inf_{F=F0+F1} (||F0||X0 + ||F1||X1).
The constrained version takes the infimum only over F0 in G0 and F1 in G1.

The paper's Lemma 1.2 establishes, for mean-zero scalar distributions phi, with extended-valued quantities allowed,
||phi||_(H^1/2 + W^1,1) equivalent (constants may depend on N) to
K(1,grad phi;G0,G1).

The equivalence uses: subtracting means from scalar summands; the mean-zero Fourier equivalence ||h||H^1/2 equivalent to ||grad h||H^-1/2; and the mean-zero L1 Poincare inequality for the W^1,1 summand.

The theorem therefore supplies F_K = grad Phi_K for which
K(1,F_K;X0,X1) <= C,
K(1,F_K;G0,G1) >= c_N K^(1/4) - C_N.
For each fixed N >= 2, the constrained-to-ambient cost ratio is unbounded. The paper's original scalar estimates have constants uniform in N,K; constants in this K-functional corollary may depend on N.

**Critical distinction:** The ambient decomposition F=F0+F1 allows arbitrary vector fields. The constrained decomposition requires each summand itself to be a gradient. The failure is precisely the failure of a uniform cost-preserving lift from the ambient decomposition to the gradient ranges.

## 3. Construction and proof dependency graph

The construction in dimension two proceeds as follows.

1. Choose lacunary frequencies lambda_i = 4^(1+i) and
   b_K(x) = K^(-1/2) sum_(i=1..K) cos(lambda_i x).
   Its L2 norm is uniformly bounded.

2. Mollify a normal sheet measure
   a_K(x,t) = (2 pi)^(-1) b_K(x) e_t rho_(epsilon_K)(t),
   epsilon_K = K^(-2) lambda_K^(-1),
   and set Phi_K = 2 Delta^(-1) div a_K using the mean-zero inverse Laplacian. Then
   grad Phi_K = 2 P a_K = 2 a_K - 2 Q a_K,
   where P is the L2 Hodge projection onto gradient fields and Q=I-P. The first term is uniformly bounded in L1; the Fourier multiplier for Q gives a uniform H^-1/2 bound for the second. This proves the ambient upper bound.

3. Define the lacunary partial-sum path
   m_j(x) = K^(-1/2) sum_(i=1..j) cos(lambda_i x).
   The fourth-moment/lacunarity estimate gives
   ||m_(j+L)-m_j||L1 >= c sqrt(L/K).
   The scale-path lemma then proves, for arbitrary f_j in L2,
   A+B >= c K^(1/4), where
   A = sum_(j<K) ||f_(j+1)-f_j||L1,
   B = (sum_(j=1..K) ||m_j-f_j||L2^2)^(1/2).
   The proof sums the increment/error inequality over j and chooses L=floor(sqrt(K)).

4. The potential is odd in the normal coordinate t. The Hilbert-valued odd critical Hardy inequality controls
   integral_0^a ||h(.,t)||L2_x^2 dt/t <= C ||h||H^1/2(T^2)^2.
   Oddness is essential; no general point trace at the critical exponent is assumed.

5. Slab averages at scales I_j=[lambda_j^(-1),2 lambda_j^(-1)], followed by tangential low-pass operators S_j, compress any scalar decomposition Phi_K=w+h into a path f_j. The W^1,1 part controls path variation; the odd Hardy inequality controls square-summed tracking error. The decomposition-compression proposition yields a lower bound of order K^(1/4), up to the profile error.

6. The normal-sheet profile estimate proves that the profile error is uniformly bounded. This finishes the two-dimensional scalar lower bound. The paper then extends the construction to all N>2.

The difficult analytic bridge is therefore not just the abstract K-functional definition. It consists of the Hodge multiplier estimate, lacunary profile estimate, odd critical Hardy estimate, and decomposition-compression estimate.

## 4. What URF currently says—and does not say

The inspected URF Core documentation and formal vocabulary cover structural admissibility, capacity/locality, graph-like invariants, entropy-depth and certificate status. The inspected URF Spine definitions are finite structural data, not definitions of fractional Sobolev spaces, vector-valued L1, Hodge projections, distributional gradients, or interpolation K-functionals.

The existing certificate schema/verifier checks certificate structure and numerical admissibility; it does not prove analytic norm estimates or identify a vector decomposition with a scalar gradient decomposition.

**Truth-test result:** URF is presently unable to decide this paper's theorem in its existing formal vocabulary. This is a demonstrated scope/formalization gap in URF, not evidence of a defect in Zhang's paper and not an independent verification of the theorem.

## 5. Minimal formalization program (ordered; no result promotion)

### Stage A — abstract functional-analytic interface

Introduce normed additive spaces and continuous linear gradient maps with explicitly typed ranges. Define the sum norm/K-functional as an infimum over decompositions. Define the gradient-constrained K-functional using the ranges of the two gradient maps. Prove the abstract scalar/constrained equivalence only after recording the exact hypotheses needed for mean-zero normalization, injectivity modulo constants, and norm equivalence.

### Stage B — finite scale-path lemma

Formalize the discrete lemma independently of Fourier analysis:
- lacunary block lower bound as an explicit hypothesis on a path m_j;
- arbitrary approximating path f_j;
- variation A and square error B;
- conclusion A+B >= c K^(1/4), with integer choice of L and constants explicit.

This is a tractable first theorem, but by itself it does not establish the paper's counterexample.

### Stage C — analytic witness

Formalize the Fourier/Hodge construction and prove the ambient upper bound, profile approximation, odd Hardy estimate, and decomposition-compression proposition. Only then can the paper's sequence be reproduced in Lean.

### Stage D — dimension extension and comparison

Prove the dimension-lifting step and connect the analytic witness to the abstract K-functional bridge. Audit all axioms and placeholders; no theorem is promoted while any required step is admitted or assumed.

## 6. Explicit boundary and status

- PAPER_THEOREM: stated by the external paper; not independently reproved here.
- ABSTRACT_BRIDGE: Lemma 1.2 is accurately transcribed; no Lean formalization yet.
- DISCRETE_SCALE_PATH: proof structure inspected; not independently machine-checked.
- HODGE_UPPER_BOUND: not independently reproduced.
- PROFILE_ESTIMATE: not independently reproduced.
- ODD_HARDY: proof structure inspected; not independently machine-checked.
- DIMENSION_EXTENSION: not independently reproduced.
- URF_CAPABILITY: current inspected URF vocabulary does not encode the required analytic objects.
- REPOSITORY_PROOF_STATUS: no Lean proof, build, or axiom audit has been produced by this work.
- EXTERNAL_ENDORSEMENT: none.

**Boundary:** URF does not yet independently verify arXiv:2610.35882.

**Next proof-bearing action:** implement Stage A in a dedicated analytic module, then prove Stage B without importing the paper's lower-bound conclusion as an axiom. Do not encode Theorem 1.1 itself as an assumed URF invariant or certificate field.

## Source

Chenye Zhang, *A Counterexample to a Bourgain–Brezis Sum-Space Estimate*, arXiv:2610.35882v1, especially Theorem 1.1, Lemma 1.2, Corollary 1.3, Lemmas 4.1–4.3, Proposition 4.4, and Proposition 5.1. https://arxiv.org/abs/2610.35882
