from pathlib import Path

NOTE = Path("docs/foundations/UJ_UNKNOWN_SECTOR_CLASSIFIER_NOTE.md").read_text()

def test_note_is_conditional():
    assert "Status: Conditional exposition note." in NOTE

def test_forbidden_overclaims_are_explicit():
    assert "CONFIRMED_UNKNOWN_SECTOR_FROM_NONDETECTION" in NOTE
    assert "CONFIRMED_METRIC_TOPOLOGY_FROM_BOUND_ONLY" in NOTE
    assert "CONFIRMED_NON_HUMAN_ORIGIN_FROM_ANOMALY" in NOTE

def test_shadow_guard_present():
    assert "Finite nondetection yields only bounds, not existence." in NOTE
    assert "No branch may promote finite absence of evidence" in NOTE

def test_nonclaims_present():
    assert "This does not prove UFO/UAP extraterrestrial origin." in NOTE
    assert "This does not prove faster-than-light travel." in NOTE
