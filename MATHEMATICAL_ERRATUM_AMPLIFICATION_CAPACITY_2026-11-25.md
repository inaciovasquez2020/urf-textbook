# Mathematical erratum — amplification and capacity

Base: `85acb9ffb54758781bda9aaa04650889f6b05b15`.

## [Global amplification barrier](manuscripts/chronos_core/Global_Amplification_Barrier.tex)

The definition must quantify over arbitrarily large input sizes, rather than hold $n$ fixed: for every fixed radius $r$ there must exist a size $n$ and graphs of that size with the stated local indistinguishability and different invariant values. For a connected graph, a radius at least $n-1$ exposes the whole graph. For disconnected graphs, equality of the sets of rooted neighborhood types at that radius need not determine component multiplicities, so the fixed-size definition is not automatically contradictory for every invariant. For the lower bound, fix an admissible deterministic algorithm whose output and halting decision are determined by its transcript. If two inputs of size $n$ have different required outputs and identical transcripts at each depth $t<cn$, neither can halt correctly before $cn$. A uniform lower bound over a class of algorithms requires witnesses with the corresponding quantifier order and a uniform positive constant; locality alone does not supply such witnesses. Identifying a singleton transcript domain with successful output requires an explicit terminal-output bridge. The conditional indistinguishability argument remains valid with these hypotheses.

## [Capacity bounds](tex/chapters/03_capacity_bounds.tex)

The depth quotient requires strictly positive capacity. At zero capacity positive initial entropy cannot reach zero by the stated cumulative bound. The original telescoping argument is unchanged. Historical sources are retained in Git history. Paper correction only; no new Lean or PDF claims.
