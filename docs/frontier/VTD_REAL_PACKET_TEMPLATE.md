# VTD Real Empirical Packet Template

Status: empirical packet template only.

This document specifies the minimal real-data packet required to test the VTD certificate.

It contains no empirical VTD data.

It does not certify a trajectory anomaly.

It does not identify a physical anti-gravity mechanism.

It is not a theorem-level URF closure claim.

## Object

\[
\mathrm{VTD}_{\mathrm{real}}
=
\left(
D,\ g_{\mathrm{cert}},\ \varepsilon_g,\ \varepsilon_{\mathrm{meas}},\ \varepsilon_F,\ \Pi
\right).
\]

Where

\[
D=\{(t_i,z_i)\}_{i=1}^{N}
\]

is real vacuum trajectory data,

\[
g_{\mathrm{cert}}
\]

is the certified local gravity reference,

\[
\varepsilon_g
\]

is the certified gravity-reference uncertainty,

\[
\varepsilon_{\mathrm{meas}}
\]

is the certified acceleration-estimator uncertainty,

\[
\varepsilon_F
\]

is the certified non-gravitational acceleration bound, and

\[
\Pi
\]

is the protocol proving the bounds apply during the trajectory.

## Required directory layout

```text
VTD_REAL_PACKET/
  README_BOUNDARY.md
  drop_real_001.csv
  g_certificate_real.yml
  eps_meas_certificate_real.yml
  eps_F_budget_real.csv
  protocol_real.md
  calibration_records/
  environment_logs/
  verifier_output.txt
Required trajectory file
File:
drop_real_001.csv
Required columns:
drop_id,t_s,z_m,z_uncertainty_m
Required conditions:
t 
1
​	
 <t 
2
​	
 <⋯<t 
N
​	
 .
z 
i
​	
 ∈R meters.
t 
i
​	
 ∈R seconds.
The file must be measured trajectory data.
It must not be reconstructed from
z(t)=z 
0
​	
 +v 
0
​	
 t− 
2
1
​	
 gt 
2
 .
Required gravity certificate
File:
g_certificate_real.yml
Required fields:
g_m_s2: ...
uncertainty_m_s2: ...
instrument: ...
instrument_serial: ...
measurement_time_utc: ...
latitude: ...
longitude: ...
altitude_m: ...
height_reference_m: ...
tide_correction_m_s2: ...
height_gradient_s_minus_2: ...
nearby_mass_correction_m_s2: ...
polar_motion_correction_m_s2: ...
operator_or_lab: ...
traceability: ...
Required bound:
∣g 
cert
​	
 −g 
true
​	
 ∣≤ε 
g
​	
 .
Required measurement-error certificate
File:
eps_meas_certificate_real.yml
Required fields:
eps_meas_m_s2: ...
estimator: local_polynomial_least_squares
degree: ...
window_samples: ...
sampling_interval_s: ...
position_noise_bound_m: ...
clock_error_bound_s: ...
length_scale_error_fraction: ...
truncation_bound: ...
confidence_level: ...
calibration_source: ...
Required bound:
∣ 
a
 (t 
⋆
 )−z 
′′
 (t 
⋆
 )∣≤ε 
meas
​	
 .
Required non-gravitational force budget
File:
eps_F_budget_real.csv
Required columns:
force_channel,acceleration_bound_m_s2,evidence,method,status
Required channels:
residual_gas_drag,...
buoyancy,...
ion_wind,...
thermal_radiometric_force,...
outgassing,...
electrostatic_patch_force,...
stray_electric_field,...
magnetic_gradient_force,...
radiation_pressure,...
acoustic_coupling,...
seismic_vibration,...
platform_vibration,...
Coriolis_term,...
centrifugal_term,...
nearby_mass_gradient,...
sensor_contact_or_tether,...
readout_backaction,...
Required total:
ε 
F
​	
 = 
j
∑
​	
 ε 
F,j
​	
 .
Required protocol
File:
protocol_real.md
Required contents:
apparatus description
vacuum pressure log
temperature log
magnetic-field log
electric-field log
vibration log
timing calibration
length-scale calibration
drop selection rule
estimator choice
window and degree choice
force-budget derivation
exclusion of reconstructed data
claim boundary
Decision rule
The real empirical VTD decision rule is
∣ 
a
 (t 
⋆
 )+g 
cert
​	
 ∣>ε 
meas
​	
 +ε 
F
​	
 +ε 
g
​	
 .
Certified residual:
R=∣ 
a
 (t 
⋆
 )+g 
cert
​	
 ∣−ε 
meas
​	
 −ε 
F
​	
 −ε 
g
​	
 .
Solved empirical condition:
R>0.
Claim boundary
If R>0, the admissible claim is only:
ordinary force balance is falsified under the supplied measurement, force, and gravity-reference bounds.
The inadmissible claim is:
mechanism-level closure is not asserted.
Missing object
The missing object is a real packet satisfying this template.
No further mathematical ingredient is missing.
