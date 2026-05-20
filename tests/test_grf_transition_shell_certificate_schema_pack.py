from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_grf_transition_shell_certificate_schema_pack_verifier_passes():
    result = subprocess.run(
        [sys.executable, "scripts/verify_grf_transition_shell_certificate_schema_pack.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "verification OK" in result.stdout


def test_complete_grf_transition_shell_certificate_schema_has_all_gates():
    artifact = json.loads(
        (ROOT / "artifacts/grf/complete_transition_shell_certificate_schema.json").read_text(
            encoding="utf-8"
        )
    )
    gates = set(artifact["required_gates"])
    assert artifact["schema_name"] == "CompleteGRFTransitionShellCertificate"
    assert artifact["status"] == "FRONTIER_OPEN_SCHEMA_ONLY"
    assert "O2_ACTUAL_DERIVATIVE_DATA" in gates
    assert "O4_MULTI_CELL_INTERVAL_PROPAGATION" in gates
    assert "O5_WEC_DEC_COMPONENT_INVENTORY" in gates
    assert "O6_MATCHING_THEOREM" in gates
    assert "O7_PHYSICAL_REALIZATION_THEOREM" in gates
    assert any("not GRF theorem-level closure" in item for item in artifact["boundary"])


def test_component_and_matching_gates_are_open():
    wec_dec = json.loads(
        (ROOT / "artifacts/grf/wec_dec_component_inventory_gate.json").read_text(
            encoding="utf-8"
        )
    )
    matching = json.loads(
        (ROOT / "artifacts/grf/matching_realization_theorem_gate.json").read_text(
            encoding="utf-8"
        )
    )
    assert wec_dec["status"] == "FRONTIER_OPEN_COMPONENT_GATE"
    assert matching["status"] == "FRONTIER_OPEN_MATCHING_REALIZATION_GATE"
    assert "rho - p_t >= 0" in wec_dec["required_components"]
    assert "O6_MATCHING_THEOREM" in matching["obligations"]
    assert "O7_PHYSICAL_REALIZATION_THEOREM" in matching["obligations"]
