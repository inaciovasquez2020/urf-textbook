from pathlib import Path

DOC = Path("docs/foundations/UJ_UNKNOWN_SECTOR_CLASSIFIER_NOTE.md")

def test_uj_unknown_sector_note_exists():
    assert DOC.exists()

def test_uj_unknown_sector_status_is_conditional():
    text = DOC.read_text()
    assert "Status: Conditional exposition note." in text

def test_uj_unknown_sector_nonclaims_locked():
    text = DOC.read_text()
    assert "This does not prove UFO/UAP extraterrestrial origin." in text
    assert "This does not prove faster-than-light travel." in text
    assert "This does not prove non-human technology." in text
    assert "This does not confirm an unknown physical sector from nondetection." in text

def test_uj_unknown_sector_forbidden_overclaims_locked():
    text = DOC.read_text()
    assert "CONFIRMED_UNKNOWN_SECTOR_FROM_NONDETECTION" in text
    assert "CONFIRMED_METRIC_TOPOLOGY_FROM_BOUND_ONLY" in text
    assert "CONFIRMED_NON_HUMAN_ORIGIN_FROM_ANOMALY" in text

def test_uj_unknown_sector_missing_object_locked():
    text = DOC.read_text()
    assert "Minimal missing object:" in text
    assert "Real calibrated multisensor event data." in text
