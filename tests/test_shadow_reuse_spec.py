import json
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_json(path: str):
    return json.loads((ROOT / path).read_text())

def load_toml(path: str):
    return tomllib.loads((ROOT / path).read_text())

def test_shadow_spec_json_toml_match():
    js = load_json("artifacts/spec/shadow_reuse_test.json")
    tm = load_toml("artifacts/spec/shadow_reuse_test.toml")
    assert js["name"] == tm["name"]
    assert js["version"] == tm["version"]
    assert js["predicate"] == tm["predicate"]
    assert js["statuses"] == tm["statuses"]
    assert js["rules"] == tm["rules"]
    assert js["global_requirements"] == tm["global_requirements"]

def test_shadow_cases_conform_to_spec():
    spec = load_json("artifacts/spec/shadow_reuse_test.json")
    cases = load_json("artifacts/spec/shadow_reuse_cases.json")
    valid_statuses = set(spec["statuses"])

    for row in cases:
        assert row["status"] in valid_statuses
        assert row["module"]
        assert row["native_object"]
        assert row["first_use_definition_required"] is True

        if row["status"] in {"Strong", "Weak"}:
            assert row["ceiling_symbol"]
            assert row["quantity_symbol"]

        if row["status"] == "NonNative":
            assert row["dual_object"]

def test_rendered_outputs_roundtrip_exist():
    for rel in [
        "artifacts/spec/shadow_reuse_test.json",
        "artifacts/spec/shadow_reuse_test.toml",
        "artifacts/spec/shadow_reuse_cases.json",
        "tools/render_shadow_reuse_cases.py",
    ]:
        assert (ROOT / rel).exists()
