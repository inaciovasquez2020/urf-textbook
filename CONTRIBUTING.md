# Contributing to URF Textbook

## Branching Model
- Create feature branches from `main`
- One structural change per branch
- No stacked fixes

## Style Policy
- All theorems must have labels
- All definitions must have labels
- Every new symbol must be added to Notation Table
- Cross-references only via \label and \ref

## Build Requirements
- pdflatex (recommended TeXLive version documented)
- bibtex
- make (if Makefile present)

## Pre-PR Checklist
- PDF builds locally without warnings
- No undefined references
- No overfull hboxes in theorem environments
- ROADMAP.md updated if structural change

## Release Discipline
- Increment version number
- Update CHANGELOG.md
- Tag release before DOI update
