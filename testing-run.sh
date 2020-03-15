#!/bin/bash
echo "TESTING CLASSIC GENERATOR:"
python3 namegen.py debug=True file=classic.txt method=classic
if [ ! $? == 0 ]; then
    echo "ERROR DETECTED"
    exit 1
fi
echo "TESTING RANDOM GENERATOR:"
python3 namegen.py debug=True file=random.txt method=random
if [ ! $? == 0 ]; then
    echo "ERROR DETECTED"
    exit 1
fi