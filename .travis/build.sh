#!/usr/bin/env bash

XTRACE=$(set +o | grep xtrace)
set -o xtrace

pip install --upgrade tox

tox -v -e pep8,py27
