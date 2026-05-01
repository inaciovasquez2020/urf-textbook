import subprocess
from pathlib import Path

def test_grf_flat_exterior_obstruction_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_flat_exterior_obstruction.py"],
        check=True,
    )

def test_grf_flat_exterior_obstruction_boundary():
    text = Path("docs/essays/GRF_2026_FLAT_EXTERIOR_OBSTRUCTION.md").read_text(encoding="utf-8")
    assert "It does not construct the Schwarzschild matching shell." in text
    assert "A computable positive-mass Schwarzschild transition-shell certificate" in text
    assert "unconditional gravitational closure" not in text.lower()
