#!/usr/bin/env bash

if ! command -v python3 &> /dev/null; then
    echo "⚠️ Python3 not found. Installing..."
    sudo apt install -y python3
fi

if ! command -v python3-venv &> /dev/null; then
    echo "⚠️ Python3-venv not found. Installing..."
    sudo apt install -y python3-venv
fi

pushd scripts &> /dev/null

python3 ../src/setup.py --fresh

popd &> /dev/null
