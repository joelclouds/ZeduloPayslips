#!/usr/bin/env bash

if ! command -v python3 &> /dev/null; then
    echo "⚠️ Python3 not found. Installing..."
    sudo apt update && sudo apt install -y python3 python3-venv
fi

sudo apt update && sudo apt install -y libreoffice

pushd scripts &> /dev/null

python3 ../src/setup.py

popd &> /dev/null
