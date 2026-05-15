from pathlib import Path
import json

doc = Path("docs/status/GRF2026_CONDITIONAL_FALSIFICATION_AUDIT_2026_05_15.md")
artifact = Path("artifacts/grf2026/conditional_falsification_audit_2026_05_15.json")

assert doc.exists(), doc
assert artifact.exists(), artifact

data = json.loads(artifact.read_text())

assert data["status"] == "CONDITIONAL_FRAMEWORK_AUDIT_ONLY"
assert data["classifications"]["Apocalypse When?"] == "CONDITIONALLY_REFUTABLE_PREMISE_LEVEL_ONLY"
assert data["classifications"]["The Gravitational Spectral Radio Forest"] == "ATTACKABLE_NOT_REFUTED"
assert data["classifications"]["How Much Can Gravitons Be Squeezed?"] == "ATTACKABLE_NOT_REFUTED"
assert data["classifications"]["Monogamous Entanglement Cheats at the Price of Complexity"] == "ALIGNED_WITH_USER_FRAMEWORK"
assert data["classifications"]["Approaching the Surface of an Exotic Compact Object"] == "BLOCKED_PENDING_FULL_TEXT"

required_nonclaims = [
    "No unconditional disproof of any GRF 2026 winning essay is claimed.",
    "No empirical/model-dependent claim is promoted to theorem-level closure.",
    "No_Phantom_Admissibility is an axiom-boundary, not a proved theorem.",
    "HII_LineSurvival_Failure requires numerical radiative-transfer or observational upper-bound input.",
    "No_Viable_SqueezedGraviton_Window requires external parameter-space closure plus SNR scan.",
    "A finite grid scan does not imply universal theorem closure without interval-cover or analytic domination."
]

for phrase in required_nonclaims:
    assert phrase in data["nonclaims"], phrase

for missing in [
    "No_Phantom_Admissibility_Proof",
    "HII_3D_RadiativeTransfer_UpperBound",
    "AxionBH_AllowedParameterSpace_Closure",
    "SqueezedGraviton_SNR_Scan",
    "ExoticCompactObject_FullText"
]:
    assert missing in data["missing_objects"], missing

text = doc.read_text()
for forbidden in [
    "disproves all",
    "unconditionally disproves",
    "GRF winners refuted",
    "paper is false",
    "theorem-level disproof"
]:
    assert forbidden.lower() not in text.lower(), forbidden

print("GRF2026 conditional falsification audit verified.")
