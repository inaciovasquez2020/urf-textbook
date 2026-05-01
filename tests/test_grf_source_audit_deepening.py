import subprocess
from pathlib import Path

def test_grf_source_audit_deepening_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_source_audit_deepening.py"],
        check=True,
    )

def test_grf_source_audit_deepening_boundary():
    text = Path("docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT_DEEPENING.md").read_text(encoding="utf-8")
    assert "A global Einstein-matter construction theorem." in text
    assert "Global Matching Lemma" in text
    assert "unconditional closure" not in text.lower()
