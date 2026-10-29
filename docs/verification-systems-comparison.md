# URF Feature Comparison and Qualified Novelty Assessment

**Status:** Comparative research note; novelty is **not established**.

## Scope

This note compares the documented aims of URF with three established approaches. It is a feature-level scoping comparison, not an exhaustive systematic review, and does not establish that the listed capabilities are unique to URF.

## Comparison

| Dimension | CODECHECK | Proof-carrying code (PCC) | Reproduction Packages | URF, as currently documented |
|---|---|---|---|---|
| Primary object | Re-execution of computational research code/workflows | A program accompanied by a machine-checkable proof of a specified safety policy | Packaged computational artifacts and environment for reproduction | Research claims, certificates, evidence, and explicit claim-status boundaries |
| Execution/build evidence | Central | May support checking but is not the defining object | Central | Used as evidence for the checked surface only |
| Formal property verification | Not the primary purpose of CODECHECK | Central for the specified policy | Not the defining requirement | Supported for selected Lean/formal artifacts; coverage varies by claim |
| Provenance / artifact metadata | Certificate and workflow context | Program/proof objects and checking context | Artifact, code, data, and environment | Hashes, provenance, receipts, and verifier outputs where supplied |
| Explicit unresolved obligations and status boundary across a research portfolio | Not its primary documented purpose | Not the primary documented purpose | Not its primary documented purpose | A stated design goal; effectiveness and coverage require independent evaluation |
| What success does **not** establish | Scientific correctness of the underlying method or conclusion | Correctness beyond the proved policy and assumptions | Scientific validity of the reproduced conclusion | A broader theorem or scientific claim beyond the exact checked artifact |

## Supporting references

1. Nüst, D. and Eglen, S. J. (2021). “CODECHECK: an open science initiative for the independent execution of computations underlying research articles.” *F1000Research*, 10:253. https://doi.org/10.12688/f1000research.51738.2
2. Appel, A. W. (2001). “Foundational proof-carrying code.” *Proceedings of the 16th Annual IEEE Symposium on Logic in Computer Science*, 247–258. https://doi.org/10.1109/LICS.2001.932501
3. Krafczyk, M. S., Shi, A., Bhaskar, A., Marinov, D., and Stodden, V. (2021). “Learning from reproducing computational results: introducing three principles and the Reproduction Package.” *Philosophical Transactions of the Royal Society A*, 379:20200069. https://doi.org/10.1098/rsta.2020.0069
4. Leipzig, J. et al. (2021). “The role of metadata in reproducible computational research.” *Patterns*, 2(9):100322. https://doi.org/10.1016/j.patter.2021.100322

## Qualified novelty statement

The Unified Rigidity Framework (URF) is a verification-first research infrastructure that aims to combine executable certificate validation, provenance and reproducibility records, and explicit tracking of claim status and unresolved obligations across mathematical and computational projects. Its proposed distinction is an integrated claim-level boundary discipline: successful execution, certificate acceptance, or compilation should not by itself promote a broader mathematical or scientific claim to proved status.

This is a **novelty hypothesis, not a finding of novelty**. The comparison above is limited to three adjacent approaches and does not rule out equivalent features in other verification, provenance, workflow, or research-assessment systems. A novelty claim would require a broader, reproducible literature and software comparison, a precise feature specification, and independent testing showing that the implementation enforces the stated boundaries on fixed releases.

## Evaluation boundary

The current comparison is documentary. It does not independently validate every URF component, establish adoption or citation impact, or show that the intended claim-status behavior is complete across the portfolio. Build and test success applies only to the specific revision and tests run.
