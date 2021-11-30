build:
	easycython fib_cy.py
	easycython *.pyx
	python setup.py build_ext -if

clean:
	@echo "Passando a vassoura"
	rm -rf __pycache__
	rm -f *.so
	rm -f f*.c
	rm -rf build
	rm -f *.html
	rm -f prof*
