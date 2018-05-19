test: FORCE
	python -m pytest test/

build: FORCE
	python setup.py sdist bdist_wheel

upload: FORCE
	twine upload dist/*

publish: build upload

FORCE: ;
