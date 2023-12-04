#!/bin/bash

#VENV_PATH="path" #path to your virtual environment
#. ./venv/bin/activate

python -m pytest test_app.py

pytest_exit_code=$?


# Check the exit code and print a message
if [ ${pytest_exit_code} -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
