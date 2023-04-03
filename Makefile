.PHONY: flake lint pre-commit pre-commit-ci

TARGET ?= ./
DJANGO_APP_NAME = doco
APP_NAME = doco

flake:
	pre-commit run flake8 -a

lint:
	pylint --rcfile=pylintrc ${DJANGO_APP_NAME} apps doco --output-format=colorized --load-plugins=pylint_django --disable=django-not-configured --django-settings-module=doco.settings

pre-commit:
	pre-commit run

pre-commit-ci:
	pre-commit run -a
