import subprocess


def test_urf_core_cslib_fmt_signal_textbook_sync():
    subprocess.run(
        ["python3", "-B", "tools/verify_urf_core_cslib_fmt_signal_textbook_sync.py"],
        check=True,
    )
