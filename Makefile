.venv: Pipfile
	PIPENV_VENV_IN_PROJECT="enabled" pipenv install --dev --skip-lock
	touch .venv


.PHONY: deps
deps: .venv


.PHONY: test
test: deps
	pipenv run coverage run -m unittest tests.py
	pipenv run coverage report -m


.PHONY: lint
lint: deps
	pipenv run pylint mkpy224o


.PHONY: ci
ci:
	${MAKE} lint
	${MAKE} test
