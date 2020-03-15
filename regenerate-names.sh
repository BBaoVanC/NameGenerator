#!/bin/bash
# if ! python3 namegen.py debug=True file=example-names/classic.txt method=classic; then
#     echo "ERROR DETECTED"
#     exit 1
# fi
if ! python3 namegen.py debug=True file=example-names/random.txt method=random; then
    echo "ERROR DETECTED"
    exit 1
fi
