import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/notes/TEMPORAL_RELAXATION_WAVE_INTUITION_BOX_2026_05_18.md"

def test_temporal_relaxation_wave_doc_boundary_tokens():
    text = DOC.read_text()
    assert "TEXTBOOK_INTUITION_BOX_ONLY" in text
    assert "This is a textbook intuition box only." in text
    assert "It may be connected to URF only if later upgraded" in text
    assert "P vs NP" in text
    assert "any Clay problem" in text

def test_temporal_relaxation_wave_envelope_bound_numeric():
    A = 3.0
    lam = 0.7
    omega = 2.3
    phi = 0.4

    for i in range(100):
        t = i / 10
        W = A * math.exp(-lam * t) * math.sin(omega * t + phi)
        e_inst = W * W
        e_env = A * A * math.exp(-2 * lam * t)
        assert e_inst <= e_env + 1e-12

def test_instantaneous_initial_energy_warning_present():
    text = DOC.read_text()
    assert "not generally valid without an additional phase assumption" in text
    assert "may vanish while later oscillations are nonzero" in text
