
.PHONY: build testpub pub clean

build:
	python3 setup.py sdist bdist_wheel

clean:
	rm -rf dist/

testpub:
	twine upload --repository testpypi dist/*

pub:
	twine upload --repository pypi dist/*

default: build
