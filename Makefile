# shamelessly adapt https://github.com/qiime2/q2-emperor/blob/master/Makefile
.PHONY: all lint test test-cov install dev clean compile-catalog deploy

PYTHON ?= python

all: ;

lint:
	flake8 microsetta_private_api

test: all
	python microsetta_private_api/LEGACY/build_db.py
	py.test

test-install: all
	# ensure the package is installed and the app is buildable. this test
	# is a passive verification that non-py essential files are part of the
	# installed entity.
	cd /  # go somewhere to avoid relative imports
	python -c "from microsetta_private_api import server; server.build_app()"

test-cov: all
	py.test --cov=microsetta_private_api

install: all
	pip install .

compile-catalog:
	pybabel compile -d microsetta_private_api/translations

dev: all
	pip install -e .

ENV_NAME = microsetta-private-api
PYTHON_VERSION = 3.11

deploy:
	conda env remove -n $(ENV_NAME) --yes 2>/dev/null; \
	conda create --yes -n $(ENV_NAME) python=$(PYTHON_VERSION) setuptools=78 && \
	conda run -n $(ENV_NAME) conda install --yes --file ci/conda_requirements.txt && \
	conda run -n $(ENV_NAME) pip install -r ci/pip_requirements.txt && \
	if [ ! -d .git ]; then export SETUPTOOLS_SCM_PRETEND_VERSION=0.0.0; fi && \
	conda run -n $(ENV_NAME) pip install -e . --no-deps

clean:
	@echo "To fully clean the test environment, manually drop the test database:"
	@echo ""
	@echo "    dropdb -U postgres -h localhost ag_test"
	@echo ""
	@echo "Then re-run 'make test' to rebuild it."
