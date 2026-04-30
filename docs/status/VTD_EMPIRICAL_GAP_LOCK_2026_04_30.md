# VTD Empirical Gap Lock — 2026-04-30

Status: repository-side preparation complete.

This document locks the remaining VTD obstruction as empirical, not mathematical and not repository-infrastructural.

## Completed repository-side layers

- VTD trajectory-anomaly certificate
- VTD trajectory verifier
- synthetic trajectory fixtures
- gravity-reference uncertainty parameter
- real packet template
- mechanism packet template
- ON/OFF mechanism-pattern verifier
- mechanism input stub
- gravity-certificate input stub
- complete mechanism input surface stubs
- real-packet readiness gate

## Current readiness result

The current packet is expected to fail readiness:

```text
vtd_packet_readiness = NOT_READY
This is correct because the packet contains STUB_ONLY and null fields.
Unique remaining object
The unique remaining object is a real empirical ON/OFF VTD mechanism packet replacing all stubs:
VTD_MECHANISM_PACKET/
  mechanism_off_real_001.csv
  mechanism_on_real_001.csv
  control_schedule_u_real.csv
  g_certificate_real.yml
  eps_meas_certificate_real.yml
  eps_F_budget_real.csv
  protocol_on_off_real.md
  calibration_records/
  environment_logs/
  blinded_replication/
Required replacement condition
All of the following must be real, measured, and traceable:
OFF trajectory data.
ON trajectory data.
control schedule.
local gravity certificate.
acceleration-estimator uncertainty certificate.
non-gravitational force budget.
ON/OFF protocol.
calibration records.
environment logs.
blinded replication records.
Required gate sequence
A real packet must pass:
python3 tools/vtd_packet_readiness.py
python3 tools/vtd_mechanism_verify.py \
  --off VTD_MECHANISM_PACKET/mechanism_off_real_001.csv \
  --on VTD_MECHANISM_PACKET/mechanism_on_real_001.csv \
  --control VTD_MECHANISM_PACKET/control_schedule_u_real.csv \
  --m REAL_MASS_KG \
  --g REAL_G_CERT \
  --eps-meas REAL_EPS_MEAS \
  --eps-F REAL_EPS_F \
  --eps-g REAL_EPS_G \
  --window 31 \
  --degree 4
Success condition
vtd_packet_readiness = READY
mechanism_packet_decision = ON_OFF_ANOMALY_PATTERN_CERTIFIED
Boundary
This lock does not certify a trajectory anomaly.
This lock does not prove an anti-gravity mechanism.
This lock does not identify a physical anti-gravity mechanism.
This lock is not a theorem-level URF closure claim.
Terminal statement
No further repository-side object is required before real empirical ON/OFF VTD input.
No further progress possible without replacing the stubs with real measured data and independent certificates.
