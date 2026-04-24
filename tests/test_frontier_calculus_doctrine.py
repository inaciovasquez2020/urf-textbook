from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_frontier_calculus_foundation_doc_exists():
    p = ROOT / "docs/foundations/FRONTIER_CALCULUS.md"
    assert p.exists()
    text = p.read_text()
    assert "Completion is not identical to solution." in text
    assert "Completion means the remaining gap has been made exact." in text
    assert "Forbidden Transition" in text

def test_frontier_calculus_adoption_doc_is_non_overclaiming():
    p = ROOT / "docs/status/FRONTIER_CALCULUS_ADOPTION.md"
    assert p.exists()
    text = p.read_text()
    assert "This file does not claim that any open theorem is solved." in text
    assert "open mathematical obstruction" in text

def test_frontier_calculus_verifier_runs():
    import subprocess, sys
    result = subprocess.run(
        [sys.executable, "tools/verify_frontier_calculus.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr + result.stdout
