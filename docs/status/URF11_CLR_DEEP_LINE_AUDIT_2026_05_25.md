# URF-11 CLR Deep Line Audit

Status: `CLR_DEEP_LINE_AUDIT_REVIEW_REQUIRED`

Scope: all git-tracked UTF-8 text files in `urf-textbook`.

Total findings: 64

Review-required findings: 59

Danger-token findings outside safe files: 0

## Findings

| Status | File | Line | Text |
|---|---:|---:|---|
| REVIEW | `README.md` | 56 | `- Entropy Depth Lower Bound` |
| REVIEW | `docs/essays/GRF_2026_EXPLICIT_ALPHA_BETA_PAIR.md` | 213 | `Equivalently, the corrected radial NEC condition is` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT.md` | 114 | `### 7. Two-function metric freedom is the correct realization frontier` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT.md` | 148 | `/ Two-function ansatz is the correct next frontier / High / Supported /` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT_DEEPENING.md` | 132 | `Supports the corrected two-function frontier and explains why the one-function ansatz was too rigid.` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex` | 144 | `for finite constants $M_1,M_2$.  Then the corresponding optical metric produces outward bending on $\Omega$ while satisfying a finite-capacity bound` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex` | 224 | `The example also shows why capacity is the correct filter.  Letting $\varepsilon\to 1$ or $R\to 0$ drives the operational cost upward.  The geometry approaches an infinite-amplification regime not because outward bending is forbidden, but because the profile becomes too sharp or too close to degeneracy.` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex` | 232 | `The correct diagnostic is therefore not:` |
| REVIEW | `docs/essays/GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex` | 236 | `The corrected diagnostic is:` |
| REVIEW | `docs/essays/GRF_2026_FLAT_EXTERIOR_OBSTRUCTION.md` | 11 | `It identifies the correct replacement exterior.` |
| REVIEW | `docs/essays/GRF_2026_FLAT_EXTERIOR_OBSTRUCTION.md` | 139 | `## Correct replacement exterior` |
| REVIEW | `docs/essays/GRF_2026_FLAT_EXTERIOR_OBSTRUCTION.md` | 168 | `## Corrected next frontier` |
| REVIEW | `docs/essays/GRF_2026_SCHWARZSCHILD_TRANSITION_PROBE.md` | 15 | `The corrected exterior target is positive-mass Schwarzschild with` |
| SAFE | `docs/examples/urf_minimal_worked_example.md` | 14 | `Compute the FO^k local type of each vertex:` |
| SAFE | `docs/examples/urf_minimal_worked_example.md` | 25 | `### Step 3 — Rigidity Trigger` |
| SAFE | `docs/examples/urf_minimal_worked_example.md` | 26 | `Large cycle-overlap rank forces divergence of local types:` |
| SAFE | `docs/examples/urf_minimal_worked_example.md` | 28 | `COR_R(G) ≥ T(k,Δ) ⇒ FO^k type diversity.` |
| SAFE | `docs/examples/urf_minimal_worked_example.md` | 37 | `local indistinguishability cannot persist under high cycle complexity.` |
| REVIEW | `docs/faq/URF_FAQ.md` | 15 | `- FO^k local types` |
| REVIEW | `docs/faq/URF_FAQ.md` | 16 | `- cycle-overlap rank` |
| REVIEW | `docs/figures/URF_FLOW_DIAGRAM.md` | 30 | `- FO^k local types` |
| REVIEW | `docs/foundations/SHADOW_COMPATIBILITY_MAP.md` | 76 | `If P is NonNative, replace Shadow(L_P) by the correct dual object.` |
| REVIEW | `docs/frontier/VTD_REAL_PACKET_TEMPLATE.md` | 128 | `tide_correction_m_s2: ...` |
| REVIEW | `docs/frontier/VTD_REAL_PACKET_TEMPLATE.md` | 130 | `nearby_mass_correction_m_s2: ...` |
| REVIEW | `docs/frontier/VTD_REAL_PACKET_TEMPLATE.md` | 131 | `polar_motion_correction_m_s2: ...` |
| REVIEW | `docs/glossary/URF_GLOSSARY.md` | 20 | `### FO^k Local Type` |
| REVIEW | `docs/glossary/URF_GLOSSARY.md` | 24 | `### Cycle-Overlap Rank (COR)` |
| REVIEW | `docs/invariants/URF_INVARIANTS.md` | 21 | `### Cycle–Overlap Rank (COR_R)` |
| REVIEW | `docs/invariants/URF_INVARIANTS.md` | 26 | `High cycle-overlap rank forces diversification of local logical types.` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 13 | `Find constants \(R(k,\Delta)\) and \(T(k,\Delta)\) such that every finite graph \(G\) with maximum degree \(\le \Delta\) satisfies` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 16 | `\operatorname{COR}_{R}(G) \ge T(k,\Delta)` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 40 | `4. an \(FO^k_R\)-type semantics map;` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 41 | `5. a proof that these obligations force type diversity.` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 64 | `\pi(D^{\mathrm{corr}}_{k,R,B}(P))` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 71 | `## CorrRank Status` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 73 | `CorrRank original-regime closure is reduced to non-tautological admissibility.` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 84 | `D^{\mathrm{corr}}_{k,R,B}(P)` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 98 | `- intended \(FO^k_R\)-type semantics data;` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 120 | `- Interaction between expansion and \(FO^k\)-type diversity.` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 135 | `- Algorithmic detection of cycle-overlap rank.` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 137 | `- Exhaustive search for minimal non-tautological CorrRank / SiMSLV instances.` |
| REVIEW | `docs/open_problems/OPEN_PROBLEMS.md` | 155 | `- unconditional CorrRank closure;` |
| REVIEW | `docs/overview/URF_ONE_PAGE.md` | 23 | `- FO^k local types` |
| REVIEW | `docs/page_audits/v0.1.2/page_11.txt` | 5 | `These lemmas establish that refinement depth corresponds to cumulative bounded information` |
| REVIEW | `docs/page_audits/v0.1.2/page_17.txt` | 4 | `The coercive spectral floor acts as a capacity barrier. Violations correspond to forbidden per-` |
| REVIEW | `docs/page_audits/v0.1.2/page_23.txt` | 3 | `Exchange Correlation Capacity (ECC) defines a threshold for macroscopic coherence.` |
| REVIEW | `docs/page_audits/v0.1.2/page_25.txt` | 3 | `This appendix records the correspondence between textbook results and formal modules in Lean.` |
| REVIEW | `docs/page_audits/v0.1.2/page_25.txt` | 5 | `•Lemmas L1–L5 correspond to information-capacity proofs.` |
| REVIEW | `docs/page_audits/v0.1.2/page_25.txt` | 6 | `•Theorems T1–T5 correspond to global rigidity reductions.` |
| REVIEW | `docs/page_audits/v0.1.2/reviews/page_5_review.md` | 13 | `The page is navigational only. It does not contain theorem statements, proofs, source-of-truth claims, or mathematical assertions requiring page-local correction.` |
| REVIEW | `docs/referee/REFEREE_GUIDE.md` | 30 | `- Cycle overlap rank / structural complexity` |
| REVIEW | `docs/review/grf_theorem_level_certificate_2026_05_20/EXTERNAL_REVIEW_LETTER.md` | 5 | `Does the repository certificate chain correctly compose the explicit transition-shell certificate, algebraic jet matching theorem, and physical realization certificate into the stated GRF theorem-level certificate closure?` |
| REVIEW | `docs/roadmap/URF_ROADMAP.md` | 23 | `- cycle-overlap rank instrumentation` |
| REVIEW | `docs/status/AI_VERIFICATION_DISCIPLINE_2026_04_25.md` | 23 | `## Correct AI role` |
| REVIEW | `docs/status/VTD_EMPIRICAL_GAP_LOCK_2026_04_30.md` | 27 | `This is correct because the packet contains STUB_ONLY and null fields.` |
| REVIEW | `docs/theorems/STABLE_TRACE_NO_GO.md` | 38 | `The correct dependency is:` |
| REVIEW | `manuscript/appendices/A_lean_map.tex` | 4 | `This appendix records the correspondence between textbook results` |
| REVIEW | `manuscript/appendices/A_lean_map.tex` | 9 | `\item Lemmas L1--L5 correspond to information-capacity proofs.` |
| REVIEW | `manuscript/appendices/A_lean_map.tex` | 10 | `\item Theorems T1--T5 correspond to global rigidity reductions.` |
| REVIEW | `manuscript/items/theorems/thm_T4.tex` | 12 | `In particular, no refinement process can create new independent information without corresponding capacity expenditure.` |
| REVIEW | `scripts/verify_grf_source_audit.py` | 15 | `    "Two-function metric freedom is the correct realization frontier",` |
| REVIEW | `tex/chapters/04_entropy_depth.tex` | 1 | `\chapter{Entropy Depth Lower Bound}` |
| REVIEW | `tex/chapters/12_cycle_overlap_rigidity.tex` | 13 | `Define \(A\) where rows correspond to cycles.` |
| REVIEW | `tex/chapters/12_cycle_overlap_rigidity.tex` | 18 | `If cycle overlap rank grows with graph size, $FO^k$-local homogeneity cannot persist.` |

## Boundary

Does not rewrite files.

Does not prove unguarded cycle-local rigidity.

Does not prove high COR forcing full FO^k type diversity.

Does not prove Chronos-RR.

Does not prove H4.1/FGL.

Does not prove P vs NP.

Does not prove any Clay problem.
