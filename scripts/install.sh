#!/usr/bin/env bash

# Check that our user has internet access
GOOGLE_DNS_IP="8.8.8.8"
CLOUDFLARE_DNS_IP="1.1.1.1"

ping -c 1 -W 2 $GOOGLE_DNS_IP > /dev/null 2>&1

if [ $? -ne 0 ]; then
    ping -c 1 -W 2 $CLOUDFLARE_DNS_IP > /dev/null 2>&1

    if [ $? -ne 0 ]; then
        echo -e "\n\n\t\tInternet access is not available!!\t Terminating..."
        exit 1
    fi
fi

sudo apt update && sudo apt install -y libreoffice

pushd scripts &> /dev/null

python3 ../src/setup.py --fresh

popd &> /dev/null
