#!/bin/bash
python3 namegen.py debug=True file=example-names/classic.txt method=classic
if [ ! $? == 0 ]; then
    echo "ERROR DETECTED"
    exit 1
fi
python3 namegen.py debug=True file=example-names/random.txt method=random
if [ ! $? == 0 ]; then
    echo "ERROR DETECTED"
    exit 1
fi
