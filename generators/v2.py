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

# require file
if not os.path.isfile("generators/ing_nounlist.txt"):
    print("ERROR: ing_nounlist.txt could not be found!")


# Generation method
def gen(count=1, debug=False):
    with open("generators/ing_nounlist.txt") as f:  # open the word list file
        words = f.readlines()  # read the file
    words = [x.strip() for x in words]  # remove the "\n" from each word

    names = list()  # prepare the names list
    n = 1  # prepare loop counter

    while count >= n:
        name1 = random.choice(words)  # choose random word
        if random.choice([True, False]):  # 50% chance
            name1 = name1.capitalize()  # capitalize the name
        name = name1[0:-1] + "q"  # change the last letter to 'q'
        if debug:  # if we should output debug information
            print("Generated name: ({}/{})".format(n-1, count),
                  end="\r")  # log message for generated names
        names.append(name)  # add name to list
        n = n + 1  # increases our loop counter

    if debug:  # if we should output debug information
        print("Generated name: ({}/{})...done".format(n-1, count))  # log msg
    return names  # return the name list
