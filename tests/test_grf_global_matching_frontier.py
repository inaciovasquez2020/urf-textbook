import subprocess
from pathlib import Path

def test_grf_global_matching_frontier_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_global_matching_frontier.py"],
        check=True,
    )

def test_grf_global_matching_frontier_boundary():
    text = Path("docs/essays/GRF_2026_GLOBAL_MATCHING_FRONTIER.md").read_text(encoding="utf-8")
    assert "This document does not prove the Global Matching Lemma." in text
    assert "A computable transition-shell certificate" in text
    assert "unconditional gravitational closure" not in text.lower()
