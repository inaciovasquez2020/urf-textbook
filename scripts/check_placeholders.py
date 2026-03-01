import pathlib, re, sys

ROOT = pathlib.Path("manuscript")
BAD = [
    r"\\Deps\s*$",
    r"\\Status\s*$",
    r"Status:\s*$",
    r"Dependencies:\s*$",
]

def main():
    tex = list(ROOT.rglob("*.tex"))
    bad_hits = []
    for p in tex:
        t = p.read_text(errors="ignore")
        for pat in BAD:
            if re.search(pat, t, flags=re.M):
                bad_hits.append((str(p), pat))
    if bad_hits:
        for f, pat in bad_hits:
            print(f"{f}: {pat}")
        sys.exit(2)

if __name__ == "__main__":
    main()
