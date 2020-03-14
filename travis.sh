#!/bin/bash
printf "TESTING CLASSIC GENERATOR:\n"
python3 namegen.py debug=True file=classic.txt method=classic
printf "TESTING RANDOM GENERATOR:\n"
python3 namegen.py debug=True file=random.txt method=random
printf "TESTING REGENERATE NAMES SCRIPT:\n"
bash ./regenerate-names.sh
