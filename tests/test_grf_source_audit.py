import subprocess
from pathlib import Path

def test_grf_source_audit_verifier_passes():
    subprocess.run(
        ["python3", "scripts/verify_grf_source_audit.py"],
        check=True,
    )

def test_grf_source_audit_has_boundary():
    text = Path("docs/essays/GRF_2026_FINITE_CAPACITY_SOURCE_AUDIT.md").read_text(encoding="utf-8")
    assert "It is not yet a full gravitational realization theorem" in text
    assert "full gravitational realization theorem is proved" not in text.lower()
