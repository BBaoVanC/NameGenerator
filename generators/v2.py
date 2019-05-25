#!/usr/bin/python3
"""
v2 Generator

by BBaoVanC

The second method of NameGenerator

Examples:
    dancinq
    Misreadinq
    Thinq
"""

# Imports
import os
import random

# if the list doesn't exist
if not os.path.isfile("generators/ing_nounlist.txt"):
    print("ERROR: ing_nounlist.txt could not be found!")


# Generation method
def gen(count=1, debug=False):
    with open("generators/ing_nounlist.txt") as f:  # open the word list file
        words = f.readlines()
    words = [x.strip() for x in words]  # remove the "\n" from each word

    names = list()
    n = 1

    while count >= n:
        name1 = random.choice(words)  # choose random word
        if random.choice([True, False]):
            name1 = name1.capitalize()
        name = name1[0:-1] + "q"  # change the last letter to 'q'
        if debug:
            print("Generated name: ({}/{})".format(n-1, count),
                  end="\r")  # log message for generated names
        names.append(name)  # add name to list
        n = n + 1  # increases our loop counter

    if debug:
        print("Generated name: ({}/{})...done".format(n-1, count))
    return names
