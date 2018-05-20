test: FORCE
	python -m pytest test/

clean: FORCE
	rm -rf dist/*

build: FORCE
	python setup.py sdist bdist_wheel

upload: FORCE
	twine upload dist/*

publish: clean build upload

FORCE: ;
