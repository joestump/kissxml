clean:
	find . -iname '*.pyc' -o -iname '*.pyo' -delete

test:
	nosetests ${ARGS}

coverage:
	$(MAKE) test ARGS="--with-coverage --cover-package=kissxml ${ARGS}"

coverage-html:
	$(MAKE) coverage ARGS="--cover-html ${ARGS}"
