import argparse, pathlib, re

def slug(s: str) -> str:
    s = re.sub(r'[^A-Za-z0-9_]+', '_', s.strip())
    s = re.sub(r'_+', '_', s).strip('_')
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kind", required=True, choices=["def","lem","thm","ex"])
    ap.add_argument("--id", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()

    outdir = pathlib.Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    fn = outdir / f"{args.kind}_{slug(args.id)}.tex"
    if fn.exists():
        raise SystemExit(f"exists: {fn}")

    header = {
        "def": "\\begin{definition}[%s]\\\\\n\\Deps \n\\Status \n\n\\end{definition}\n",
        "lem": "\\begin{lemma}[%s]\\\\\n\\Deps \n\\Status \n\n\\end{lemma}\n",
        "thm": "\\begin{theorem}[%s]\\\\\n\\Deps \n\\Status \n\n\\end{theorem}\n",
        "ex":  "\\begin{example}[%s]\\\\\n\\Deps \n\\Status \n\n\\end{example}\n",
    }[args.kind] % args.title

    fn.write_text(header)

if __name__ == "__main__":
    main()
