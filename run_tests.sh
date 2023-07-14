#!/bin/bash

chmod u+x run_tests.sh

# Loop through test numbers 1 to 7
for test_num in {1..7}
do
    test_file="test_${test_num}.txt"
    echo -e "\n\nRunning ${test_file}"
    python3 production.py "$test_file"
done