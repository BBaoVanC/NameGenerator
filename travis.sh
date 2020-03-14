#!/bin/bash
printf "TESTING CLASSIC GENERATOR:"
python3 namegen.py debug=True file=classic.txt method=classic
printf "TESTING RANDOM GENERATOR:"
python3 namegen.py debug=True file=random.txt method=random
printf "TESTING REGENERATE NAMES SCRIPT:"
bash ./regenerate-names.sh
