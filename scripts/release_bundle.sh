set -euo pipefail

TAG="${1:?tag required}"
mkdir -p releases

pdflatex -interaction=nonstopmode -halt-on-error -output-directory=releases manuscript/main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=releases manuscript/main.tex

mv -f releases/main.pdf "releases/URF_Textbook_${TAG}.pdf"

python3 scripts/sha256_manifest.py --out "releases/SHA256_${TAG}.json" --include releases
