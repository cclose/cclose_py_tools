#!/bin/bash

pip3 install --use-feature=in-tree-build --editable .[test]

echo "Linting..."
flake8 --max-line-length=88 tests hello_python

echo "Testing..."
pytest
