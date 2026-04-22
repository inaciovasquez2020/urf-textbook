# URF Textbook Quickstart

This is the shortest path from clone to a first successful local verification pass.

## Requirements

- `git`
- `bash`
- `python3`
- `make`

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/urf-textbook.git
cd urf-textbook
```

## 2. Check tools

```bash
python3 --version
git --version
make --version
```

## 3. Run canonical checks

```bash
[ -d tests ] && python3 -m pytest -q
```

## 4. Review the main documentation surfaces

- `README.md`
- `STATUS.md`
- `ROADMAP.md`
- `RELEASE.md`
- `docs/index/DOCUMENTATION_INDEX.md`
- `TOOLCHAIN.md`

## 5. Build entrypoints

- `make pdf`
- `make clean`
- `make release`

## 6. Next steps

- detailed setup: `docs/SETUP_GUIDE.md`
- contribution policy: `CONTRIBUTING.md`
