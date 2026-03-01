TAG ?= dev

pdf:
	mkdir -p releases releases/chapters releases/appendices
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=releases manuscript/main.tex
	pdflatex -interaction=nonstopmode -halt-on-error -output-directory=releases manuscript/main.tex

clean:
	rm -rf releases

release:
	./scripts/release_bundle.sh $(TAG)
