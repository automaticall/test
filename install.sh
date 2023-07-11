#!/bin/bash
echo "up to  date  apt cache"
sudo apt update

pipenv run pip run -r requirements.txt
