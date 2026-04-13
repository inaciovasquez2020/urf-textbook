from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

def test_shadow_of_infinity_completion_values():
    proc = subprocess.run(
        [sys.executable, "tools/render_shadow_of_infinity_completion_2026_04_13.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(proc.stdout)
    artifact = json.loads(
        Path("artifacts/status/shadow_of_infinity_completion_2026_04_13.json").read_text(encoding="utf-8")
    )

    assert payload == artifact
    assert payload["components"]["canonical_placement"] == 1
    assert payload["components"]["definition_lock"] == 1
    assert payload["components"]["toolkit_registry_lock"] == 1
    assert payload["components"]["clay_registry_lock"] == 1
    assert payload["components"]["value_returning_test_layer"] == 1
    assert payload["components"]["artifact_emission_layer"] == 1
    assert payload["components"]["repo_cleanliness_after_run"] == 0
    assert payload["verified_toolkit_count"] == 8
    assert payload["verified_clay_count"] == 6
    assert payload["registry_score"] == "14/14"
    assert payload["registry_complete"] is True
    assert payload["module_completion_percent"] == 85.71
    assert payload["status_lock_present"] is True
