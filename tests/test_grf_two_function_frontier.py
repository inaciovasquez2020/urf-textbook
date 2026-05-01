import subprocess
from pathlib import Path

def test_grf_two_function_frontier_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_two_function_frontier.py"],
        check=True,
    )

def test_grf_two_function_frontier_boundary():
    text = Path("docs/essays/GRF_2026_FINITE_CAPACITY_TWO_FUNCTION_FRONTIER.md").read_text(encoding="utf-8")
    assert "The next missing object is an explicit bounded pair" in text
    assert "unconditional gravitational realization" not in text.lower()
