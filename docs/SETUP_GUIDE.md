# Setup Guide

This guide is for contributors who want a reliable local environment for URF Textbook.

## Prerequisites

```bash
python3 --version
git --version
make --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment
- Make

## Clone

```bash
git clone https://github.com/inaciovasquez2020/urf-textbook.git
cd urf-textbook
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Verification

```bash
[ -d tests ] && python3 -m pytest -q
```

## Common build entrypoints

```bash
make pdf
make clean
make release
```

## Recommended edit loop

```bash
git pull --ff-only origin main
[ -d tests ] && python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `README.md`
- `STATUS.md`
- `ROADMAP.md`
- `RELEASE.md`
- `TOOLCHAIN.md`
- `docs/index/DOCUMENTATION_INDEX.md`
