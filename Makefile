ROOT=manuscript/main.tex
PDF=urf-textbook.pdf

all:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(ROOT)
	mv manuscript/main.pdf $(PDF)

clean:
	latexmk -C
	rm -f $(PDF)

release:
	latexmk -pdf -interaction=nonstopmode -halt-on-error $(ROOT)
        mv manuscript/main.pdf urf-textbook-$(TAG).pdf
