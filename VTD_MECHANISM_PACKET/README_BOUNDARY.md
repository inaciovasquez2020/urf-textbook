# VTD Mechanism Packet Input Stub

Status: input stub only.

This directory is the staging location for the real empirical ON/OFF VTD mechanism packet.

It contains no real empirical VTD mechanism data unless the required files are inserted by measurement.

It does not prove an anti-gravity mechanism.

It does not identify a physical anti-gravity mechanism.

It is not a theorem-level URF closure claim.

## Required real files

- mechanism_off_real_001.csv
- mechanism_on_real_001.csv
- control_schedule_u_real.csv
- g_certificate_real.yml
- eps_meas_certificate_real.yml
- eps_F_budget_real.csv
- protocol_on_off_real.md
- calibration_records/
- environment_logs/
- blinded_replication/

## Passing command

```bash
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
Required success line
mechanism_packet_decision = ON_OFF_ANOMALY_PATTERN_CERTIFIED
Missing object
A real empirical ON/OFF packet satisfying this stub is missing.
