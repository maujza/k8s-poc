SHELL := /bin/bash
PYTHON_VERSION := 3.9.10
PIPENV_VERSION := 2022.8.24
PRECOMMIT_VERSION := 2.15.0
DOCKER_IMAGE_NAME := simple_app
DOCKER_CONTAINER_NAME := simple_app
DOCKER_PORT := 8080

.PHONY: build-env pre-commit setup clean

build-env:
	@pyenv install $(PYTHON_VERSION) --skip-existing
	@pyenv local $(PYTHON_VERSION)
	@pip install pipenv==$(PIPENV_VERSION)
	@pipenv install --python $(PYTHON_VERSION)
	@pipenv install pre-commit==$(PRECOMMIT_VERSION)
	@$(MAKE) pre-commit

pre-commit:
	@pipenv run pre-commit uninstall
	@pipenv run pre-commit install

setup: build-env
	@curl -o simple_app/app/utils/emoji.json https://raw.githubusercontent.com/iamcal/emoji-data/master/emoji.json
	@docker build --no-cache -t $(DOCKER_IMAGE_NAME) .
	@docker run --env-file .env --rm --name $(DOCKER_CONTAINER_NAME) -p $(DOCKER_PORT):$(DOCKER_PORT) $(DOCKER_IMAGE_NAME)

clean:
	@docker stop $(DOCKER_CONTAINER_NAME)
	@docker rm $(DOCKER_CONTAINER_NAME)
