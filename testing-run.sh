#!/bin/bash
echo "TESTING CLASSIC GENERATOR:"
if ! python3 namegen.py debug=True file=classic.txt method=classic; then
    echo "ERROR DETECTED"
    exit 1
fi
echo "TESTING RANDOM GENERATOR:"
if ! python3 namegen.py debug=True file=random.txt method=random; then
    echo "ERROR DETECTED"
    exit 1
fi