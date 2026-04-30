# VTD Mechanism Packet Template

Status: Template only.

This document specifies the weakest packet required to move from a VTD trajectory-anomaly certificate to mechanism-level evidence.

It contains no empirical VTD mechanism data.

It does not prove an anti-gravity mechanism.

It does not identify a physical anti-gravity mechanism.

It is not a theorem-level URF closure claim.

## Mechanism packet object

A mechanism packet is

\[
M_{\mathrm{mech}}
=
(D_{\mathrm{off}},D_{\mathrm{on}},u(t),g_{\mathrm{cert}},\varepsilon_g,\varepsilon_{\mathrm{meas}},\varepsilon_F,\Pi).
\]

Here

\[
D_{\mathrm{off}}
\]

is the vacuum trajectory dataset with the declared mechanism OFF,

\[
D_{\mathrm{on}}
\]

is the vacuum trajectory dataset with the declared mechanism ON,

\[
u(t)
\]

is the declared control schedule,

\[
g_{\mathrm{cert}}
\]

is the certified local gravitational reference,

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

is the protocol proving the bounds apply during OFF/ON switching.

## Required directory layout

```text
VTD_MECHANISM_PACKET/
  README_BOUNDARY.md
  mechanism_off_real_001.csv
  mechanism_on_real_001.csv
  control_schedule_u_real.csv
  g_certificate_real.yml
  eps_meas_certificate_real.yml
  eps_F_budget_real.csv
  protocol_on_off_real.md
  calibration_records/
  environment_logs/
  verifier_output_off.txt
  verifier_output_on.txt
  blinded_replication/
Required tests
The packet is admissible only if all conditions hold:
OFF condition:
∣ 
a
  
off
​	
 (t 
⋆
 )+g 
cert
​	
 ∣≤ε 
meas
​	
 +ε 
F
​	
 +ε 
g
​	
 .
ON condition:
∣ 
a
  
on
​	
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
Stable sign condition:
sgn( 
a
  
on
​	
 (t 
⋆
 )+g 
cert
​	
 )
is reproducible across independent ON trials.
Control-response condition:
u 
1
​	
 <u 
2
​	
 ⟹R(u 
1
​	
 )≤R(u 
2
​	
 )
or a predeclared reproducible non-monotone response law is supplied.
Force-budget condition:
∣F 
non-gravity
​	
 (t)∣/m≤ε 
F
​	
 
during OFF, ON, and switching intervals.
Gravity-reference condition:
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
Blind-replication condition:
At least one independent blinded packet reproduces OFF non-rejection and ON rejection under the same certificate format.
Mechanism-level admissibility threshold
A mechanism packet is admissible only if
D 
off
​	
 

⊨VTD rejection
and
D 
on
​	
 ⊨VTD rejection
under the same certified bounds.
Boundary
This template can support mechanism-level evidence only after real empirical packets satisfy every required object and test.
It cannot by itself prove mechanism-level closure.
It cannot by itself prove anti-gravity.
It cannot by itself identify a physical mechanism.
Missing object
The missing object is a real ON/OFF mechanism packet satisfying this template.
No further mathematical ingredient is missing.

Plain-token guard: R(u_1) <= R(u_2).
