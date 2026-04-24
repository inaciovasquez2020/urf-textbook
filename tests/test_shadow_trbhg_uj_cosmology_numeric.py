import importlib.util
from pathlib import Path

MODULE_PATH = Path("tools/shadow_trbhg_uj_numeric.py")
spec = importlib.util.spec_from_file_location("shadow_trbhg_uj_numeric", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ObservationScores = mod.ObservationScores

C_KM_S = 299_792.458
H0_KM_S_MPC = 70.0

def redshift(lambda_observed_nm: float, lambda_rest_nm: float) -> float:
    return lambda_observed_nm / lambda_rest_nm - 1.0

def low_z_hubble_velocity_km_s(z: float) -> float:
    return C_KM_S * z

def low_z_hubble_distance_mpc(z: float) -> float:
    return low_z_hubble_velocity_km_s(z) / H0_KM_S_MPC

def finite_cosmological_shadow_score(z: float) -> float:
    return z / (1.0 + z)

def test_cosmology_redshift_values_are_numerically_locked():
    z = redshift(lambda_observed_nm=984.42, lambda_rest_nm=656.28)

    assert round(z, 6) == 0.500000
    assert round(low_z_hubble_velocity_km_s(z), 3) == 149896.229
    assert round(low_z_hubble_distance_mpc(z), 3) == 2141.375
    assert round(finite_cosmological_shadow_score(z), 6) == 0.333333

def test_large_cosmological_shadow_does_not_imply_unknown_sector():
    z = redshift(lambda_observed_nm=984.42, lambda_rest_nm=656.28)
    shadow_score = finite_cosmological_shadow_score(z)

    o = ObservationScores(
        sensor_coherence=shadow_score,
        trajectory_reconstruction=shadow_score,
        artifact_exclusion=1.0,
        environmental_exclusion=1.0,
    )

    assert shadow_score == 1.0 / 3.0
    assert mod.classify(o) == "INSUFFICIENT_DATA"
    assert mod.guard_holds(o)

def test_cosmological_nondetection_remains_bound_only():
    o = ObservationScores(nondetection_only=True)

    assert mod.classify(o) == "UNKNOWN_SECTOR_BOUND_ONLY"
    assert mod.guard_holds(o)

def test_cosmology_like_boundary_signal_requires_nonair_witnesses_for_upgrade():
    o = ObservationScores(
        sensor_coherence=0.95,
        trajectory_reconstruction=0.95,
        artifact_exclusion=0.95,
        environmental_exclusion=0.95,
    )

    assert mod.classify(o) == "NON_AIR_CANDIDATE"
    assert mod.guard_holds(o)

def test_cosmology_like_metric_topology_candidate_requires_all_extra_witnesses():
    o = ObservationScores(
        sensor_coherence=0.95,
        trajectory_reconstruction=0.95,
        artifact_exclusion=0.95,
        environmental_exclusion=0.95,
        causal_anomaly=0.95,
        conservation_closure=0.95,
        repeatability=0.95,
        independent_instrumentation=0.95,
    )

    assert mod.classify(o) == "METRIC_TOPOLOGY_CANDIDATE"
    assert mod.guard_holds(o)

def test_time_reversal_shadow_has_orientation_not_existence_content():
    z = redshift(lambda_observed_nm=984.42, lambda_rest_nm=656.28)
    forward = mod.theta_shadow_orientation(z, tau=1)
    reversed_ = mod.theta_shadow_orientation(z, tau=-1)

    assert forward == 0.5
    assert reversed_ == -0.5
    assert forward + reversed_ == 0.0

    o = ObservationScores(time_reversal_template=True)
    assert mod.classify(o) == "TIME_REVERSAL_SHADOW_TEMPLATE"
    assert mod.guard_holds(o)
