#!/bin/bash
ruff check --fix
ruff format .
isort --profile black --verbose .
