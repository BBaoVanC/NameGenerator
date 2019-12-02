#!/usr/bin/python3
"""
Classic Generator

by BBaoVanC

The classic method for NameGenerator

Examples:
    TheAssignmentanatorifier_90
    Coinifier_313
    COMPONENTGUY290

Copyright (C) 2019 BBaoVanC
"""

# Imports
import os
import random
import lib.progress

# following block is for a file requirement
if not os.path.isfile("generators/desiquintans.com_nounlist.txt"):
    print("ERROR: desiquintans.com_nounlist.txt could not be found!")


# Generation method
def gen(count=1, debug=False):
    """Generate names using the classic method."""
    with open("generators/desiquintans.com_nounlist.txt") as f:  # open file
        words = f.readlines()  # read all lines into a list
        # closing the file is not required, the with block does that for us
    words = [x.strip("\n") for x in words]  # remove the "\n" from each word
    wsuffixes = ["ator", "man", "guy", "ifier", "anator", ""]  # suffixes
    wprefixes = ["Mr", "The", ""]  # prefixes
    names = list()  # initialize the names list variable
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels2 = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels3 = ['a', 'i', 'o', 'u']  # custom vowel list
    n = 1  # prepare loop counter
    while count >= n:  # name generation loop
        word_pre = random.choice(words)  # choose a random word
        word_pre = word_pre.capitalize()  # capitalize the first letter
        wprefix = random.choice(wprefixes)  # choose a random prefix
        wsuffix = random.choice(wsuffixes)  # choose a random suffix
        wsuffix2 = wsuffix  # prepare wsuffix2
        if wsuffix == "ator" or wsuffix == "anator":  # if the suffix is either
            if random.choice([True, False, False]):  # 1/3 chance
                wsuffix2 = wsuffix + "ifier"  # add the extra suffix of "ifier"

        # if we should make the name all caps
        caps = random.choice([True, False, False, False])
        if caps:  # if we are going to make it all caps
            wprefix = wprefix.upper()  # set the prefix to all caps
            word_pre = word_pre.upper()  # set the word to all caps
            wsuffix2 = wsuffix2.upper()  # set the suffix to all caps
            if len(wprefix) > 0:  # if there is a prefix
                wprefix = wprefix + "_"  # underscore at the end of the prefix

        if word_pre[-1] in vowels3:  # if the word ends in aiouy
            if wsuffix == 'ator' or wsuffix == 'anator':  # grammar fix
                wsuffix = 'nator'  # set the suffix to "nator"

        # create a string 'word' which adds the 3 parts together
        word = str(wprefix) + str(word_pre) + str(wsuffix2)
        # choose if there should be an underscore before the number at the end
        space = random.choice(["_", "", ""])
        # choose a random number to have at the end
        number = random.randint(0, 999)
        # puts together the different parts of the username
        name = str(word) + str(space) + str(number)
        if debug:  # if we should output debug information
            print(lib.progress.genbar(curprg=n-1, maxprg=count), end="\r")
        names.append(name)  # add name to list of generated names
        n = n + 1  # increases our loop counter

    if debug:  # if we should output debug information
        print(lib.progress.genbar(curprg=n-1, maxprg=count) + "...done")
    return names  # return the generated names
