#!/bin/bash

#VENV_PATH="path" #path to your virtual environment
#source "${VENV_PATH}/bin/activate" #activate your virtual environment
#
#cd /path/to/your/test # Navigate to the directory containing your test.py

pytest_result=$(pytest) # Run the test suite using pytest

pytest_exit_code=$?


# Check the exit code and print a message
if [ ${pytest_exit_code} -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed."
    exit 1
fi
