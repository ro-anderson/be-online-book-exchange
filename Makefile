.PHONY: clean update-install-pre-dependencies install-poetry source-env \
config-poetry-source install-python-dependencies-local install_local init_local test run \
create_db

SHELL=/bin/bash
.DEFAULT_GOAL := help

-include .env

## Removes project virtual env
clean:
	rm -rf .venv build dist **/*.egg-info .pytest_cache node_modules .coverage

## exist to source env, ingore if not exists
update-install-pre-dependencies:
	-apt-get update && apt-get install --no-install-recommends -y curl

## Install poetry in the system
install-poetry: update-install-pre-dependencies
	curl -sSL https://install.python-poetry.org | python3 - && poetry self update --preview 1.2.0b3

## exist to source env, ingore if not exists
source-env:
	-source .env

## CI config Sync with emcasa pypi
ci-config-poetry-source: source-env
	-eval 'poetry config http-basic.emcasa ${PYPI_USERNAME} ${PYPI_PASSWORD}'

## Sync with emcasa pypi
config-poetry-source: source-env ci-config-poetry-source
	-poetry source add emcasa https://pypi.emcasa.com/simple/\
	&& poetry config http-basic.emcasa ${PYPI_USERNAME} ${PYPI_PASSWORD}

## Install python dependencies
install-python-dependencies-local:
	poetry install --without debug
	poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg --hook-type pre-push

## Install abd config poetry
install_local: install-poetry config-poetry-source install-python-dependencies-local

## init project
init_local: clean install_local

## Run tests
test:
	poetry run python -m pytest -v

## Start local server
run:
	poetry run  uvicorn app.main:app --host ${API_HOST} --port ${API_PORT} --reload

## Create sqlite DB
create_db:
	python create_db.py

## Shows this help text
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
