#!/bin/bash
echo "TESTING CLASSIC GENERATOR:"
python3 namegen.py debug=True file=classic.txt method=classic
echo "TESTING RANDOM GENERATOR:"
python3 namegen.py debug=True file=random.txt method=random
echo "TESTING REGENERATE NAMES SCRIPT:"
