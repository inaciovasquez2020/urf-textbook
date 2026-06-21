#!/usr/bin/env python3
from pathlib import Path
import json

artifact_path = Path("artifacts/urf_core/cslib_fmt_signal_textbook_sync_2026_06_21.json")
doc_path = Path("docs/status/URF_CORE_CSLIB_FMT_SIGNAL_TEXTBOOK_SYNC_2026_06_21.md")

data = json.loads(artifact_path.read_text())
doc = doc_path.read_text()

assert data["status"] == "URF_CORE_CSLIB_FMT_SIGNAL_TEXTBOOK_SYNC_2026_06_21"
assert data["source_repo"] == "urf-core"
assert data["source_pr"] == 474
assert data["source_main_commit"] == "857e954"
assert data["textbook_effect"] == "status_sync_only"
assert "CSLIB_FMT_FULL_FORMULA_RADIUS_EXTERNAL_STATUS_SIGNAL_OK" in data["source_statuses"]
assert "URF_CORE_FULL_PYTEST_BASELINE_BLOCKERS_OK" in data["source_statuses"]
assert "no new theorem" in data["boundary"]
assert "no URF-core repair" in data["boundary"]
assert "no CSLIB-FMT proof import" in data["boundary"]

assert "Status: `URF_CORE_CSLIB_FMT_SIGNAL_TEXTBOOK_SYNC_2026_06_21`" in doc
assert "commit `857e954`" in doc
assert "CSLIB_FMT_FULL_FORMULA_RADIUS_EXTERNAL_STATUS_SIGNAL_OK" in doc
assert "URF_CORE_FULL_PYTEST_BASELINE_BLOCKERS_OK" in doc
assert "status synchronization note only" in doc
assert "no new theorem" in doc

print("URF_CORE_CSLIB_FMT_SIGNAL_TEXTBOOK_SYNC_OK")
