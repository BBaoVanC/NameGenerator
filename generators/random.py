#!/usr/bin/python3
"""
Random Generator

by BBaoVanC

Generates a name by using random characters!

Examples:
    KkC44zZIkJ6b
    Mw6xAKYulItJ
    qK1Kpv89fJj1
"""

# Imports
import random


# Generation method
def gen(count=1, debug=False, length=12):
    names = list()  # prepare blank names list
    n = 1  # prepare loop counter

    while count >= n:
        name = ""  # prepare name variable
        for _ in range(length):  # for each chracter in the name
            charset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z", "_", "0", "1", "2", "3", "4", "5",
                       "6", "7", "8", "9"]  # character set
            char = random.choice(charset)  # choose a random character
            cap = random.choice([True, False])  # choose capitalization
            if cap:  # if it should be capitalized
                char = char.capitalize()  # capitalize the letter
            name = name + str(char)  # add the character to the name
        if debug:  # if we should output debug information
            print("Generated name: ({}/{})".format(n-1, count),
                  end="\r")  # log message for generated names
        names.append(name)  # add the name to the name list
        n = n + 1  # increase counter

    if debug:  # if we should output debug information
        print("Generated name: ({}/{})...done".format(n-1, count))  # log msg
    return names  # return the name list
