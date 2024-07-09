#!/bin/bash

set -e

python setup.py sdist bdist_wheel
pip uninstall -y gsc_cli
pip install .
