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
import logging

logging.basicConfig(level=logging.INFO)


# Generation method
def gen(count=1, debug=False, length=12):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    names = list()
    n = 1

    while count >= n:
        name = ""
        for i in range(length):
            charset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z", "_", "0", "1", "2", "3", "4", "5",
                       "6", "7", "8", "9"]
            char = random.choice(charset)
            cap = random.choice([True, False])
            if cap:
                char = char.capitalize()
            name = name + str(char)
        logging.debug("Generated name: " + name)
        names.append(name)
        n = n + 1

    return names
