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
import logging

logging.basicConfig(level=logging.INFO)
# if the list doesn't exist
if not os.path.isfile("generators/ing_nounlist.txt"):
    logging.critical("ing_nounlist.txt could not be found!")


# Generation method
def gen(count=1, debug=False):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

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
        logging.debug("Generated name: " + name)
        names.append(name)  # add name to list
        n = n + 1  # increases our loop counter

    return names
