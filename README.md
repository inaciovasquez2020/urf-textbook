<!-- VERIFIED_FRONTIER_TRACKING_EXPLANATION:BEGIN -->
## Verified Frontier Tracking Explanation Layer

This repository is the human-readable explanation layer for **Verified Frontier Tracking**.

It explains the public URF/Chronos stack in ordinary research terms:

| Question | Answer supplied here |
|---|---|
| What is the system? | A verification-first research framework for tracking hard claims without overclaiming |
| Why does it matter? | It separates proved results from conditional bridges, interface objects, and open frontiers |
| How should it be read? | Start with definitions, then status labels, then examples, then technical repositories |
| What should not be inferred? | No theorem-level closure is claimed unless explicitly named and proved |

Boundary: this repository explains the framework and its status discipline. It is not, by itself, a proof that every referenced frontier is solved.
<!-- VERIFIED_FRONTIER_TRACKING_EXPLANATION:END -->


<!-- VERIFIED_FRONTIER_TRACKING_DOOR:BEGIN -->
## Verified Frontier Tracking Explanation Layer

This repository is the human-readable explanation layer for **Verified Frontier Tracking**.

Its role is to translate the public URF/Chronos stack into readable form:

| Question | Answer supplied here |
|---|---|
| What is the system? | A verification-first research framework for tracking hard claims without overclaiming |
| Why does it matter? | It separates proved results from conditional bridges, interface objects, and open frontiers |
| How should it be read? | Start with definitions, then status labels, then examples, then technical repositories |
| What should not be inferred? | No theorem-level closure is claimed unless explicitly named and proved |

Boundary: this repository explains the framework and its status discipline. It is not, by itself, a proof that every referenced frontier is solved.
<!-- VERIFIED_FRONTIER_TRACKING_DOOR:END -->

Unified Rigidity Framework Textbook
Build
make pdf
make clean
Release
make release

DOI: 10.5281/zenodo.18826977

---

## Structural Map

The URF Textbook is organized as follows:

- Core Invariants (Entropy, Capacity, Depth, Spectral Gap)
- Operational Rigidity Principle
- Non-Amplification and Capacity Bounds
- Entropy Depth Lower Bound
- Terminal Obstructions (Cyclone)
- Applications and Reductions

See:
- `tex/chapters/structure_overview.tex`
- `tex/appendices/dependency_graph.tex`
- `ROADMAP.md` for planned extensions.

---

## Citation and Archival

This repository is part of the **Unified Rigidity Framework (URF)** research program.

For citation information see:

docs/citations/CITATION.md

A DOI archival record is available via Zenodo for reproducible citation
of repository releases.


---

## Documentation

A complete documentation map is available here:

docs/index/DOCUMENTATION_INDEX.md

This includes:

- framework overview
- invariants and structural lemmas
- open problems
- reproducibility artifacts
- bibliography and related work
- worked examples
- referee guide


- [IECP Test Protocol](docs/navier_stokes/IECP_test_protocol.md)
- [IECP Frontier](docs/navier_stokes/IECP_frontier.md)

- [Complexity / Chronos / EntropyDepth Frontier](docs/navier_stokes/ENTROPYDEPTH_frontier.md)

- [IECP Local Branching Lemma Sketch](docs/navier_stokes/IECP_local_branching_sketch.md)
- [Finite Local-Pattern Compression Lemma Sketch](docs/navier_stokes/ENTROPYDEPTH_local_pattern_sketch.md)
- [Hard Family Specification](docs/navier_stokes/HARDFAMILY_spec.md)
- [Dependency Graph](docs/navier_stokes/DEPENDENCY_graph.md)

- [Chronos Core](docs/navier_stokes/CHRONOS_core.md)

## Current reference routing

This repository is the exposition and release-facing documentation layer for URF.

Current reference authority for URF definitions, theorem statements, dependency ledgers, and closure claims remains in `urf-core`.

Community-additive examples, tests, implementations, and non-current reference extensions belong in `urf-core-community`.

## Independent Forks and Verification

Independent forks, reproducibility checks, adversarial review, issues, and pull requests are welcome.

Start here:

- [Call for Independent Forks and Verification](CALL_FOR_INDEPENDENT_FORKS.md)
- [Current reference discussion thread](https://github.com/inaciovasquez2020/urf-textbook/discussions/52)

## External status

This repository is governed by [`docs/status/EXTERNAL_STATUS_LOCK.md`](docs/status/EXTERNAL_STATUS_LOCK.md). Build success, CI success, dashboards, ledgers, axioms, admits, `sorry`, or placeholder witnesses do not constitute theorem-level closure.
## Documentation Source-of-Truth Status

Status: Documentation / Textbook Surface

This repository is an exposition surface. It does not independently prove mathematical claims.

Theorem-status rule:
- Every theorem-level claim must inherit from a buildable formal source repository.
- The inherited source must identify repository, commit or release, file path, theorem/artifact name, and status label.
- Build success, LaTeX success, dashboards, badges, ledgers, or textbook exposition do not constitute theorem-level proof.

Source-of-truth document:
- `docs/status/SOURCE_OF_TRUTH_2026_04_27.md`
