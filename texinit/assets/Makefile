source = "@filename"

all:
	-@pdflatex ${source}
	-@pdflatex ${source} >/dev/null
	-@rm -f ${source}.log ${source}.aux ${source}.out
	-@echo "\"${source}\" is successfully compiled."
