from dataclasses import dataclass

FORBIDDEN = {
    "CONFIRMED_UNKNOWN_SECTOR",
    "CONFIRMED_NON_HUMAN_ORIGIN",
    "CONFIRMED_METRIC_ENGINEERING",
    "CONFIRMED_TRAVERSABLE_WORMHOLE",
}

ALLOWED = {
    "MUNDANE",
    "SENSOR_ARTIFACT",
    "ENVIRONMENTAL_ARTIFACT",
    "AIR_DOMAIN_ADMISSIBLE",
    "NON_AIR_CANDIDATE",
    "UNKNOWN_SECTOR_BOUND_ONLY",
    "METRIC_TOPOLOGY_CANDIDATE",
    "TIME_REVERSAL_SHADOW_TEMPLATE",
    "INSUFFICIENT_DATA",
}

@dataclass(frozen=True)
class ObservationScores:
    sensor_coherence: float = 0.0
    trajectory_reconstruction: float = 0.0
    artifact_exclusion: float = 0.0
    environmental_exclusion: float = 0.0
    causal_anomaly: float = 0.0
    conservation_closure: float = 0.0
    repeatability: float = 0.0
    independent_instrumentation: float = 0.0
    nondetection_only: bool = False
    air_domain_admissible: bool = False
    artifact_likelihood: float = 0.0
    environmental_likelihood: float = 0.0
    time_reversal_template: bool = False

def clamp01(x: float) -> float:
    return max(0.0, min(1.0, float(x)))

def non_air_score(o: ObservationScores) -> float:
    return min(
        clamp01(o.sensor_coherence),
        clamp01(o.trajectory_reconstruction),
        clamp01(o.artifact_exclusion),
        clamp01(o.environmental_exclusion),
    )

def metric_topology_score(o: ObservationScores) -> float:
    return min(
        non_air_score(o),
        clamp01(o.causal_anomaly),
        clamp01(o.conservation_closure),
        clamp01(o.repeatability),
        clamp01(o.independent_instrumentation),
    )

def classify(o: ObservationScores) -> str:
    if o.nondetection_only:
        return "UNKNOWN_SECTOR_BOUND_ONLY"

    if clamp01(o.artifact_likelihood) >= 0.70:
        return "SENSOR_ARTIFACT"

    if clamp01(o.environmental_likelihood) >= 0.70:
        return "ENVIRONMENTAL_ARTIFACT"

    if o.air_domain_admissible:
        return "AIR_DOMAIN_ADMISSIBLE"

    if metric_topology_score(o) >= 0.85:
        return "METRIC_TOPOLOGY_CANDIDATE"

    if non_air_score(o) >= 0.80:
        return "NON_AIR_CANDIDATE"

    if o.time_reversal_template:
        return "TIME_REVERSAL_SHADOW_TEMPLATE"

    return "INSUFFICIENT_DATA"

def guard_holds(o: ObservationScores) -> bool:
    return classify(o) in ALLOWED and classify(o) not in FORBIDDEN

def theta_shadow_orientation(value: float, tau: int = 1) -> float:
    if tau not in (-1, 1):
        raise ValueError("tau must be +1 or -1")
    return tau * float(value)

if __name__ == "__main__":
    cases = {
        "bound_only": ObservationScores(nondetection_only=True),
        "non_air": ObservationScores(
            sensor_coherence=0.91,
            trajectory_reconstruction=0.88,
            artifact_exclusion=0.93,
            environmental_exclusion=0.86,
        ),
        "metric_topology": ObservationScores(
            sensor_coherence=0.93,
            trajectory_reconstruction=0.91,
            artifact_exclusion=0.95,
            environmental_exclusion=0.90,
            causal_anomaly=0.88,
            conservation_closure=0.87,
            repeatability=0.89,
            independent_instrumentation=0.92,
        ),
    }

    for name, obs in cases.items():
        label = classify(obs)
        assert label in ALLOWED
        assert label not in FORBIDDEN
        print(f"{name}: {label}")
