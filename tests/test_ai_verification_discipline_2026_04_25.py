from pathlib import Path


DOC = Path("docs/status/AI_VERIFICATION_DISCIPLINE_2026_04_25.md")


def test_ai_verification_discipline_exists_and_defines_scope():
    text = DOC.read_text(encoding="utf-8")

    assert "CANONICAL AI-INTERPRETATION GUARDRAIL" in text
    assert "status-controlled executable verification system" in text
    assert "not as a narrative research project" in text
    assert "does not add new mathematical claims" in text


def test_ai_verification_discipline_locks_artifact_grounding():
    text = DOC.read_text(encoding="utf-8")

    assert "AGENTS.md" in text
    assert "AI_ENTRYPOINT" in text
    assert "docs/status/" in text
    assert "verifier scripts in `tools/`" in text
    assert "certificate data" in text
    assert "CI or local verifier output" in text


def test_ai_verification_discipline_blocks_overclaiming():
    text = DOC.read_text(encoding="utf-8")

    assert "must not report the theorem as closed" in text
    assert "must not be reported as closed" in text
    assert "README-only overclaiming" in text
    assert "artifact-grounded summaries" in text


def test_ai_verification_discipline_safe_summary_template():
    text = DOC.read_text(encoding="utf-8")

    assert "This repository certifies [specific executable/status surface]." in text
    assert "It does not certify [explicit boundary]." in text
    assert "The current remaining gap is [status-file boundary], if any." in text
