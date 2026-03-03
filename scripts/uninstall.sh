#!/usr/bin/env bash

pushd scripts &> /dev/null

python3 ../src/setup.py --uninstall

popd &> /dev/null
