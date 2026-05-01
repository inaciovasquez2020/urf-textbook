import subprocess
from pathlib import Path

def test_grf_explicit_alpha_beta_pair_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_explicit_alpha_beta_pair.py"],
        check=True,
    )

def test_grf_explicit_alpha_beta_pair_boundary():
    text = Path("docs/essays/GRF_2026_EXPLICIT_ALPHA_BETA_PAIR.md").read_text(encoding="utf-8")
    assert "This is a local annular certificate." in text
    assert "The next missing object is a global matching lemma" in text
    assert "unconditional gravitational closure" not in text.lower()
