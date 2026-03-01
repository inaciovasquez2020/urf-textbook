# Recommended TeX Toolchain

To ensure deterministic builds:

- TeXLive 2023 (or fixed yearly release)
- pdflatex (not lualatex/xelatex unless specified)
- bibtex
- makeindex
- tikz compatible version

Recommended Docker base (optional):
texlive/texlive:TL2023

Build locally:
./build.sh
