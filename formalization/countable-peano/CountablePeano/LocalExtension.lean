import Mathlib

/-!
# Endpoint-controlled extension on a metric space

This is the local extension problem isolated from Lemma 5.5 of
Brazas--Pavešić, *Countable Models of One-Dimensional Peano Continua*.

Given disjoint closed subsets E and F of a metric space X, the theorem below
constructs a continuous function H : X → [0,1] whose zero set is exactly E
and whose one set is exactly F. Thus H takes values strictly between 0 and 1
off E ∪ F. Composing H with a parametrization of a closed arc gives the
endpoint-controlled extension needed on the closure of each open lifting
piece.

The construction uses distances to E and F, with a harmless positive
constant substituted when either set is empty. It does not assume that
either set is nonempty.
-/

noncomputable def distanceToSet {X : Type*} [MetricSpace X]
    (s : Set X) (x : X) : ℝ :=
  if hs : s.Nonempty then Metric.infDist x s else 1

theorem continuous_distanceToSet {X : Type*} [MetricSpace X]
    (s : Set X) : Continuous (distanceToSet s) := by
  classical
  by_cases hs : s.Nonempty
  · simpa [distanceToSet, hs] using
      (Metric.continuous_infDist (s := s))
  · simp [distanceToSet, hs]

theorem distanceToSet_nonneg {X : Type*} [MetricSpace X]
    (s : Set X) (x : X) : 0 ≤ distanceToSet s x := by
  classical
  by_cases hs : s.Nonempty
  · simp [distanceToSet, hs, Metric.infDist_nonneg]
  · simp [distanceToSet, hs]

theorem distanceToSet_eq_zero_iff {X : Type*} [MetricSpace X]
    (s : Set X) (hs : IsClosed s) (x : X) :
    distanceToSet s x = 0 ↔ x ∈ s := by
  classical
  by_cases hne : s.Nonempty
  · simpa [distanceToSet, hne] using
      (hs.mem_iff_infDist_zero hne (x := x)).symm
  · have hnot : ∀ y, y ∉ s := by
      intro y hy
      exact hne ⟨y, hy⟩
    simp [distanceToSet, hne, hnot]

theorem distanceToSet_pos_of_not_mem {X : Type*} [MetricSpace X]
    (s : Set X) (hs : IsClosed s) (hne : s.Nonempty) {x : X}
    (hx : x ∉ s) : 0 < distanceToSet s x := by
  have hx' : x ∉ closure s := by
    simpa [hs.closure_eq] using hx
  simpa [distanceToSet, hne] using
    (Metric.infDist_pos_iff_notMem_closure hne).mp hx'

/-- A continuous interval-valued separator with exact endpoint preimages. -/
theorem exists_continuous_endpoint_separator
    {X : Type*} [MetricSpace X] {E F : Set X}
    (hE : IsClosed E) (hF : IsClosed F) (hEF : Disjoint E F) :
    ∃ H : X → ℝ,
      Continuous H ∧
      (∀ x, 0 ≤ H x ∧ H x ≤ 1) ∧
      (∀ x, H x = 0 ↔ x ∈ E) ∧
      (∀ x, H x = 1 ↔ x ∈ F) := by
  let dE : X → ℝ := distanceToSet E
  let dF : X → ℝ := distanceToSet F
  let H : X → ℝ := fun x => dE x / (dE x + dF x)
  have hdE : Continuous dE := continuous_distanceToSet E
  have hdF : Continuous dF := continuous_distanceToSet F
  have hsum : ∀ x, 0 < dE x + dF x := by
    intro x
    have hEn := distanceToSet_nonneg E x
    have hFn := distanceToSet_nonneg F x
    by_contra hnot
    have hz : dE x + dF x = 0 :=
      le_antisymm (le_of_not_gt hnot) (add_nonneg hEn hFn)
    have hparts := (add_eq_zero_iff_of_nonneg hEn hFn).mp hz
    have hxE : x ∈ E := (distanceToSet_eq_zero_iff E hE x).mp hparts.1
    have hxF : x ∈ F := (distanceToSet_eq_zero_iff F hF x).mp hparts.2
    exact (Set.disjoint_left.mp hEF) hxE hxF
  refine ⟨H, ?_, ?_, ?_, ?_⟩
  · exact hdE.div (hdE.add hdF) (fun x => (hsum x).ne')
  · intro x
    have hEn := distanceToSet_nonneg E x
    have hFn := distanceToSet_nonneg F x
    have hs := hsum x
    constructor
    · exact div_nonneg hEn (le_of_lt hs)
    · apply (div_le_iff₀ hs).2
      dsimp [dE, dF]
      nlinarith
  · intro x
    change dE x / (dE x + dF x) = 0 ↔ x ∈ E
    constructor
    · intro hx
      have hzero : dE x = 0 :=
        (div_eq_zero_iff).mp hx |>.resolve_right (hsum x).ne'
      exact (distanceToSet_eq_zero_iff E hE x).mp hzero
    · intro hx
      have hzero : dE x = 0 :=
        (distanceToSet_eq_zero_iff E hE x).mpr hx
      simp [hzero]
  · intro x
    change dE x / (dE x + dF x) = 1 ↔ x ∈ F
    constructor
    · intro hx
      have heq : dE x = 1 * (dE x + dF x) :=
        (div_eq_iff (hsum x).ne').mp hx
      have hzero : dF x = 0 := by nlinarith
      exact (distanceToSet_eq_zero_iff F hF x).mp hzero
    · intro hx
      have hzero : dF x = 0 :=
        (distanceToSet_eq_zero_iff F hF x).mpr hx
      have hpos : 0 < dE x := by
        simpa [hzero] using hsum x
      simp [hzero, (ne_of_gt hpos)]
