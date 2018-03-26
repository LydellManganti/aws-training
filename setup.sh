#!/bin/bash

virtualenv=${1:-app}

virtualenv .venv/$virtualenv
source ./.venv/$virtualenv/bin/activate
pip install -r requirements.txt
