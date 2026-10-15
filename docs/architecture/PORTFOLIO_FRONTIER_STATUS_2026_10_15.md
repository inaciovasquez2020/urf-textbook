# Portfolio Frontier Status — 2026-10-15

This is a dated navigation receipt for current gates. It does not combine separate project results into a master theorem.

## Confirmed updates

### Yang–Mills HS surrogate

- PR #49 merged: https://github.com/inaciovasquez2020/yang-mills-hs-gap-cert/pull/49
- Merge commit: `558a3cf43a0ab6b9f0b686c3d65ef52638ba5437`
- Established: the stored finite-truncation surrogate fails at `P=20`.
- Not established: operator Hilbert–Schmidt divergence, failure of every HS approach, or a Yang–Mills mass-gap proof.

### DFM-MKC / ACT DR6

- Source-recovery PR #317 merged: https://github.com/inaciovasquez2020/dfm-mkc-cosmology/pull/317
- Merge commit: `eb8758ffc04d3e08a9f8d3301f4c31447ad1e58f`
- PR #318 is the active source-audit receipt: https://github.com/inaciovasquez2020/dfm-mkc-cosmology/pull/318
- Deeper source inspection found a historical 135-entry LCDM bandpower candidate, split 45 TT-like / 45 TE-like / 45 EE-like rows. It was numerically materialized within tolerance but explicitly not promoted; the raw-byte digest differed from the earlier candidate digest.
- The ACT-lite likelihood source applies SACC windows to `Cl` obtained with `ell_factor=True), scales by `A_act^{-2}), and applies `P_act^{-1}` per E-mode leg. The 135-row route's precise remaining gate is the exact ACT-lite configuration, nuisance-parameter point or fit rule, data/model provenance, and reproducible likelihood output—not a generic assumption that this CMB-only likelihood uses the full multifrequency MFLike foreground model.
- The historical internal quadratic-form value `153.61808801048306` is not an authenticated ACT-lite likelihood result and is not a DFM-MKC comparison.
- Not established: promoted baseline vector, reproducible official likelihood run, DFM-MKC 135-row prediction, empirical validation, or any cosmological resolution.

### Radiative Rigidity

- PR #26 remains open: https://github.com/inaciovasquez2020/radiative-rigidity/pull/26
- Current head: `1f5034b326859b1e8764a0c914fdf554b768c800`
- Direct row check confirms 49 stored `delta_odd` values match `(1-R)/(1+R)` within absolute tolerance `1e-12).
- The `epsilon` column matches current `main`; synthetic `LOWQ2_VIRTUAL` rows are excluded from the empirical scan.
- The head has no check runs or commit statuses. The repository's latest returned Actions history is from 2026-05-22, so the missing verification is not a new passing run that was overlooked. Do not merge until the regression suite is run and verified through a usable path.
- Rank-one factorization remains unproved; next mathematical test is source-backed empirical 2-by-2 minors with uncertainties and normalization groups handled.

### Chronos / GfE

- Corrected AEH half-normalization P/Q/GQQ certificate remains the controlling finite-block result.
- Exact finite algebraic claims include P0/Q0 ranks, idempotence, the nonzero commutator `[G_-1,P0]=G_-1`, and guarded GQQ rank/determinant behavior.
- Conditional finite-block inverse boundedness follows on a compact domain that excludes denominator poles and keeps `|Delta| >= d > 0`.
- Not established: invariant projector beyond P0, Fredholm resolution, uniform complementary-dynamics estimate, or horizon/outgoing closure.

### URF-core

- Canonical residual remains the unconditional witness-family mathematics boundary in `docs/status/URF_REMAINING_FRONTIER_CANONICAL.md`.
- Bounded witness verification does not establish the unrestricted witness-family theorem.
- Next decisive result: unconditional witness-family theorem or a counterexample to the proposed implication.

### Poincaré

- The candidate local potential `Phi(T)=sum_v |d(v)-6|` is not monotone under the current move definitions.
- This rejects that candidate descent argument only.
- Global descent/obstruction across nondecreasing or recurrent branches and the terminal zero-defect class remain open.

## Portfolio-level interpretation

The shared method is finite representation, local law, invariant/defect, explicit obstruction, and certified consequence. That methodological similarity does not imply a shared theorem or cross-project closure.

## Freeze rule

Do not broaden claims merely because tests pass or receipts are merged. Upgrade a claim only when its own missing mathematical or empirical bridge is discharged and recorded in the owning repository.
