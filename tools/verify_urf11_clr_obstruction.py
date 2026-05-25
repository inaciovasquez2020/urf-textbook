#!/usr/bin/env python3
import json
from pathlib import Path
from collections import deque

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/examples/urf_minimal_worked_example.md"
ART = ROOT / "artifacts/urf11/clr_full_diversity_obstruction_2026_05_25.json"

REQUIRED_DOC_TOKENS = [
    "CLR_FULL_DIVERSITY_OPEN_COUNTEREXAMPLE_OBSTRUCTION_PRESENT",
    "\\operatorname{COR}_R(G)",
    "T_{\\mathrm{full}}(k,\\Delta,r,R)=+\\infty",
    "T_{\\mathrm{guarded}}(k,\\Delta,r,R)=0",
    "G_m=C_m\\square C_m",
    "m^2-1",
    "\\operatorname{SymBreak}_{k,r}(G)",
    "Does not prove unguarded cycle-local rigidity",
    "Does not prove Chronos-RR",
    "Does not prove H4.1/FGL",
    "Does not prove P vs NP",
    "Does not prove any Clay problem",
]

def torus_vertices(m):
    return [(i, j) for i in range(m) for j in range(m)]

def torus_neighbors(m, v):
    i, j = v
    return [
        ((i + 1) % m, j),
        ((i - 1) % m, j),
        (i, (j + 1) % m),
        (i, (j - 1) % m),
    ]

def canonical_edge(a, b):
    return tuple(sorted((a, b)))

def torus_edges(m):
    edges = set()
    for v in torus_vertices(m):
        for w in torus_neighbors(m, v):
            edges.add(canonical_edge(v, w))
    return sorted(edges)

def square_cycle_edges(m, i, j):
    a = (i, j)
    b = ((i + 1) % m, j)
    c = ((i + 1) % m, (j + 1) % m)
    d = (i, (j + 1) % m)
    return [
        canonical_edge(a, b),
        canonical_edge(b, c),
        canonical_edge(c, d),
        canonical_edge(d, a),
    ]

def gf2_rank(rows):
    basis = {}
    for x in rows:
        y = x
        while y:
            p = y.bit_length() - 1
            if p not in basis:
                basis[p] = y
                break
            y ^= basis[p]
    return len(basis)

def torus_square_rank(m):
    edge_index = {e: idx for idx, e in enumerate(torus_edges(m))}
    rows = []
    for i in range(m):
        for j in range(m):
            bitrow = 0
            for e in square_cycle_edges(m, i, j):
                bitrow ^= 1 << edge_index[e]
            rows.append(bitrow)
    return gf2_rank(rows)

def rooted_ball_signature(m, r, root):
    q = deque([(root, 0)])
    seen = {root: 0}
    while q:
        v, d = q.popleft()
        if d == r:
            continue
        for w in torus_neighbors(m, v):
            if w not in seen:
                seen[w] = d + 1
                q.append((w, d + 1))

    ri, rj = root
    def rel(v):
        i, j = v
        di = (i - ri) % m
        dj = (j - rj) % m
        if di > m // 2:
            di -= m
        if dj > m // 2:
            dj -= m
        return (di, dj)

    rel_vertices = sorted(rel(v) for v in seen)
    rel_set = set(rel_vertices)
    rel_edges = []
    for v in seen:
        for w in torus_neighbors(m, v):
            if w in seen:
                a, b = rel(v), rel(w)
                if a < b:
                    rel_edges.append((a, b))
    return (tuple(rel_vertices), tuple(sorted(rel_edges)))

def verify_obstruction(m=9, r=2):
    assert m > 2 * r + 2
    vertices = torus_vertices(m)
    assert all(len(set(torus_neighbors(m, v))) == 4 for v in vertices)
    signatures = {rooted_ball_signature(m, r, v) for v in vertices}
    assert len(signatures) == 1
    assert torus_square_rank(m) == m * m - 1

def main():
    doc = DOC.read_text()
    for token in REQUIRED_DOC_TOKENS:
        assert token in doc, token

    data = json.loads(ART.read_text())
    assert data["status"] == "CLR_FULL_DIVERSITY_OPEN_COUNTEREXAMPLE_OBSTRUCTION_PRESENT"
    assert data["thresholds"]["T_full(k,Delta,r,R)"] == "infinity"
    assert data["thresholds"]["T_guarded(k,Delta,r,R)"] == 0
    assert data["required_obstruction_family"] == "C_m square C_m"
    for token in [
        "does_not_prove_unguarded_cycle_local_rigidity",
        "does_not_prove_high_COR_forces_full_FOk_type_diversity",
        "does_not_prove_Chronos_RR",
        "does_not_prove_H4_1_FGL",
        "does_not_prove_P_vs_NP",
        "does_not_prove_any_Clay_problem",
    ]:
        assert token in data["boundary"], token

    verify_obstruction()
    print("OK: URF-11 CLR obstruction registry verified")

if __name__ == "__main__":
    main()
