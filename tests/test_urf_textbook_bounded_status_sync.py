from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/status/URF_TEXTBOOK_BOUNDED_STATUS_SYNC_2026_06_09.md"
ART = ROOT / "artifacts/status/urf_textbook_bounded_status_sync_2026_06_09.json"

def test_bounded_status_sync_doc_boundary():
    text = DOC.read_text()
    assert "BOUNDED_STATUS_SYNC_ONLY" in text
    assert "repository_native_bounded_status_certificate" in text
    assert "concreteAnalyticPackageNextBuildStopLockCertificate" in text
    assert "does not claim" in text
    assert "P vs NP" in text
    assert "Clay-problem closure" in text

def test_bounded_status_sync_artifact_boundary():
    data = json.loads(ART.read_text())
    assert data["status"] == "BOUNDED_STATUS_SYNC_ONLY"
    assert data["next_admissible_object"] == "Stop"
    assert len(data["synchronized_objects"]) == 2
    assert "P_vs_NP" in data["claims_not_made"]
    assert "Clay_problem_closure" in data["claims_not_made"]
