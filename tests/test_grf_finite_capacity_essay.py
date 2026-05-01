import subprocess
from pathlib import Path

def test_grf_finite_capacity_essay_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_finite_capacity_essay.py"],
        check=True,
    )

def test_grf_finite_capacity_essay_exists():
    path = Path("docs/essays/GRF_2026_FINITE_CAPACITY_SPACETIME_DEFLECTION.tex")
    assert path.exists()
    text = path.read_text(encoding="utf-8")
    assert "Finite-capacity outward deflection" in text
    assert "Outward deflection is admissible only when" in text
