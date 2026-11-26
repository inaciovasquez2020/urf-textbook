# Mathematical erratum — 2026-11-25

Base: 7c3bf8743c4d5a8f3274b605a3040b6c92e12bea

Source: [Cycle-Overlap Rigidity](tex/chapters/12_cycle_overlap_rigidity.tex).

The original cycle-space dimension formula used the connected-graph expression for arbitrary graphs. The corrected expression adds the number of components. The spanning-forest basis proves it.

The historical global rigidity statement did not define its overlap rank. For the interpretation as a span of embedded local cycle spaces, even toroidal square grids give a counterexample: their local cycle rank grows linearly in vertex count, but vertex transitivity gives identical rooted types. The chapter now states the exact counterexample and separates per-ball bounds from global span bounds.

The original source is retained in Git history (blob 0f047e132b4f67ed234db6eb0f139efd26f060ae). This is a mathematical paper correction, not a new Lean verification. Existing PDF artifacts have not been regenerated or audited.
