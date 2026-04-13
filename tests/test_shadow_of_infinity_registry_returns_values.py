from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

def test_shadow_of_infinity_registry_returns_values():
    proc = subprocess.run(
        [sys.executable, "tools/render_shadow_of_infinity_registry_values.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    values = json.loads(proc.stdout)
    artifact = json.loads(
        Path("artifacts/foundations/shadow_of_infinity_registry_values.json").read_text(encoding="utf-8")
    )

    assert values == artifact
    assert values["shadow_formulation_present"] is True
    assert values["toolkit_total"] == 8
    assert values["toolkit_present"] == 8
    assert values["toolkit_missing"] == 0
    assert values["clay_total"] == 6
    assert values["clay_present"] == 6
    assert values["clay_missing"] == 0
    assert values["registry_complete"] is True
