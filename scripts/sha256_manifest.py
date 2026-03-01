import argparse, hashlib, json, os, pathlib

def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1<<20), b""):
            h.update(b)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", required=True)
    ap.add_argument("--include", nargs="+", default=["releases"])
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    files = []
    for inc in args.include:
        base = (root / inc).resolve()
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file():
                rel = str(p.relative_to(root))
                files.append((rel, sha256_file(p)))

    files.sort()
    obj = {"root": str(root), "files": [{"path": r, "sha256": s} for r, s in files]}
    pathlib.Path(args.out).write_text(json.dumps(obj, indent=2) + "\n")

if __name__ == "__main__":
    main()
