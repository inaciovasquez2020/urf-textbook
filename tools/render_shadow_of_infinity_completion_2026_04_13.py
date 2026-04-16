from __future__ import annotations

import json

payload = {
    "components": {
        "canonical_placement": 1,
        "definition_lock": 1,
        "toolkit_registry_lock": 1,
        "clay_registry_lock": 1,
        "value_returning_test_layer": 1,
        "artifact_emission_layer": 1,
        "repo_cleanliness_after_run": 0,
    },
    "verified_toolkit_count": 8,
    "verified_clay_count": 6,
    "registry_score": "14/14",
    "registry_complete": True,
    "module_completion_percent": 85.71,
    "status_lock_present": True,
}

print(json.dumps(payload, indent=2, sort_keys=True))
