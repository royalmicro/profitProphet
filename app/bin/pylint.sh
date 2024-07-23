#!/bin/bash
set -e 

find . -name "*.py" | xargs pylint