#!/bin/bash
set -e

export FLASK_APP=__init__.py  # Or the entry point of your Flask app
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
export PYTHONPATH=$(pwd)

python3.12 -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m flask run 
