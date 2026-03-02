# URF Textbook Repository Status

## Canonical Branches

### main
- Canonical textbook branch
- Fully structured book (Chapters 0–10)
- Cross-reference hardened
- Proof-compressed
- Release lineage: v0.5.x and beyond

### proof-compression-pass
- Centralized EntropyDepth theorem
- Removed redundant proofs
- Fully merged into main (historical)

### journal-core-extract
- Article-length extraction (~20–40 pages)
- Self-contained EntropyDepth + Linear Wall
- Intended for journal submission
- Not merged into main

---

## Release Policy

- Releases are created from `main` only.
- Use `gh release create` (never manual tag push).
- No force-pushing tags.
- No mixing journal branch into textbook branch.

---

## Structural Guarantees

- Single authoritative EntropyDepth theorem
- Spectral coercivity centralized
- No duplicated proofs
- All references symbolic (`\ref`)
- Index build artifacts ignored
- Structural DAG integrated

---

## Current State

Repository is structurally stable.

Next evolution layers:
- Journal submission packaging
- Diagrammatic expansion
- Exercise solutions volume
- Research monograph expansion
