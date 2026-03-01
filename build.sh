#!/usr/bin/env bash
set -e

MAIN="main.tex"

pdflatex -interaction=nonstopmode $MAIN
bibtex main || true
pdflatex -interaction=nonstopmode $MAIN
pdflatex -interaction=nonstopmode $MAIN

echo "Build complete."
