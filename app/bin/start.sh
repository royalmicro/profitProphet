#!/bin/bash

export FLASK_APP=run.py  # Or the entry point of your Flask app
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000

flask run
