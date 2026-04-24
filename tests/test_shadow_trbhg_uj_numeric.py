import importlib.util
from pathlib import Path

MODULE_PATH = Path("tools/shadow_trbhg_uj_numeric.py")
spec = importlib.util.spec_from_file_location("shadow_trbhg_uj_numeric", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ObservationScores = mod.ObservationScores

def test_nondetection_only_is_bound_only_not_existence():
    o = ObservationScores(nondetection_only=True)
    assert mod.classify(o) == "UNKNOWN_SECTOR_BOUND_ONLY"
    assert mod.guard_holds(o)

def test_non_air_upgrade_requires_four_numerical_witnesses():
    o = ObservationScores(
        sensor_coherence=0.90,
        trajectory_reconstruction=0.86,
        artifact_exclusion=0.91,
        environmental_exclusion=0.82,
    )
    assert mod.non_air_score(o) == 0.82
    assert mod.classify(o) == "NON_AIR_CANDIDATE"
    assert mod.guard_holds(o)

def test_missing_one_non_air_witness_blocks_upgrade():
    o = ObservationScores(
        sensor_coherence=0.95,
        trajectory_reconstruction=0.94,
        artifact_exclusion=0.93,
        environmental_exclusion=0.20,
    )
    assert mod.non_air_score(o) == 0.20
    assert mod.classify(o) == "INSUFFICIENT_DATA"
    assert mod.guard_holds(o)

def test_metric_topology_candidate_requires_extra_four_witnesses():
    o = ObservationScores(
        sensor_coherence=0.92,
        trajectory_reconstruction=0.91,
        artifact_exclusion=0.93,
        environmental_exclusion=0.90,
        causal_anomaly=0.89,
        conservation_closure=0.88,
        repeatability=0.87,
        independent_instrumentation=0.86,
    )
    assert mod.metric_topology_score(o) == 0.86
    assert mod.classify(o) == "METRIC_TOPOLOGY_CANDIDATE"
    assert mod.guard_holds(o)

def test_metric_topology_downgrades_to_non_air_if_extra_witness_missing():
    o = ObservationScores(
        sensor_coherence=0.92,
        trajectory_reconstruction=0.91,
        artifact_exclusion=0.93,
        environmental_exclusion=0.90,
        causal_anomaly=0.89,
        conservation_closure=0.20,
        repeatability=0.87,
        independent_instrumentation=0.86,
    )
    assert mod.metric_topology_score(o) == 0.20
    assert mod.classify(o) == "NON_AIR_CANDIDATE"
    assert mod.guard_holds(o)

def test_artifact_and_environmental_artifacts_block_upgrade():
    sensor = ObservationScores(
        sensor_coherence=1.0,
        trajectory_reconstruction=1.0,
        artifact_exclusion=1.0,
        environmental_exclusion=1.0,
        artifact_likelihood=0.90,
    )
    environmental = ObservationScores(
        sensor_coherence=1.0,
        trajectory_reconstruction=1.0,
        artifact_exclusion=1.0,
        environmental_exclusion=1.0,
        environmental_likelihood=0.90,
    )
    assert mod.classify(sensor) == "SENSOR_ARTIFACT"
    assert mod.classify(environmental) == "ENVIRONMENTAL_ARTIFACT"

def test_air_domain_admissibility_blocks_non_air_upgrade():
    o = ObservationScores(
        sensor_coherence=1.0,
        trajectory_reconstruction=1.0,
        artifact_exclusion=1.0,
        environmental_exclusion=1.0,
        air_domain_admissible=True,
    )
    assert mod.classify(o) == "AIR_DOMAIN_ADMISSIBLE"
    assert mod.guard_holds(o)

def test_time_reversal_shadow_orientation_is_antisymmetric():
    x = 3.75
    assert mod.theta_shadow_orientation(x, tau=1) == 3.75
    assert mod.theta_shadow_orientation(x, tau=-1) == -3.75
    assert mod.theta_shadow_orientation(x, tau=1) + mod.theta_shadow_orientation(x, tau=-1) == 0.0

def test_forbidden_labels_are_never_returned_on_grid():
    values = [0.0, 0.25, 0.5, 0.8, 0.85, 1.0]
    for a in values:
        for b in values:
            o = ObservationScores(
                sensor_coherence=a,
                trajectory_reconstruction=b,
                artifact_exclusion=1.0,
                environmental_exclusion=1.0,
                causal_anomaly=a,
                conservation_closure=b,
                repeatability=1.0,
                independent_instrumentation=1.0,
            )
            assert mod.classify(o) not in mod.FORBIDDEN
            assert mod.classify(o) in mod.ALLOWED
