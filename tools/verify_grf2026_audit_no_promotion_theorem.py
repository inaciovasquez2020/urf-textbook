from pathlib import Path
import json

doc = Path("docs/status/GRF2026_AUDIT_NO_PROMOTION_THEOREM_2026_05_15.md")
artifact = Path("artifacts/grf2026/audit_no_promotion_theorem_2026_05_15.json")

assert doc.exists(), doc
assert artifact.exists(), artifact

text = doc.read_text()
data = json.loads(artifact.read_text())

assert data["status"] == "VERIFIED_STATUS_GUARD_ONLY"
assert data["theorem"] == "GRF2026_Audit_NoPromotion"

allowed = {
    "CONDITIONALLY_REFUTABLE_PREMISE_LEVEL_ONLY",
    "ATTACKABLE_NOT_REFUTED",
    "ALIGNED_WITH_USER_FRAMEWORK",
    "BLOCKED_PENDING_FULL_TEXT",
}

assert set(data["allowed_classifications"]) == allowed
assert set(data["targets"].values()).issubset(allowed)

required_targets = {
    "Apocalypse When?": "CONDITIONALLY_REFUTABLE_PREMISE_LEVEL_ONLY",
    "The Gravitational Spectral Radio Forest": "ATTACKABLE_NOT_REFUTED",
    "How Much Can Gravitons Be Squeezed?": "ATTACKABLE_NOT_REFUTED",
    "Monogamous Entanglement Cheats at the Price of Complexity": "ALIGNED_WITH_USER_FRAMEWORK",
    "Approaching the Surface of an Exotic Compact Object": "BLOCKED_PENDING_FULL_TEXT",
}

assert data["targets"] == required_targets

for key in [
    "no_unconditional_disproof_promotion",
    "no_theorem_level_refutation_promotion",
    "no_solved_status_promotion",
    "no_empirical_to_theorem_promotion",
]:
    assert data["proved_guard"][key] is True, key

required_nonclaims = [
    "This is a repository status-guard theorem only.",
    "No physical statement is proved.",
    "No empirical falsification is proved.",
    "No mathematical disproof of any GRF 2026 essay is proved.",
    "No Chronos-RR closure is proved.",
    "No H4.1/FGL closure is proved.",
    "No P vs NP result is proved.",
    "No Clay-problem closure is proved.",
]

for phrase in required_nonclaims:
    assert phrase in data["nonclaims"], phrase
    assert phrase in text, phrase

for missing in [
    "No_Phantom_Admissibility_Proof",
    "HII_3D_RadiativeTransfer_UpperBound",
    "AxionBH_AllowedParameterSpace_Closure",
    "SqueezedGraviton_SNR_Scan",
    "ExoticCompactObject_FullText",
]:
    assert missing in data["missing_objects_preserved"], missing
    assert missing in text, missing

for forbidden in [
    "unconditionally disproves",
    "unconditional disproof of",
    "theorem-level refutation of",
    "GRF winners refuted",
    "paper is false",
    "falsifies all",
    "proves the essays wrong",
    "solves GRF",
]:
    assert forbidden.lower() not in text.lower(), forbidden
    assert forbidden.lower() not in json.dumps(data).lower(), forbidden

print("GRF2026 audit no-promotion theorem verified.")
