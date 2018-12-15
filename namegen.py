"""
Random Username Generator

by BBaoVanC

Generates a file with 100 different usernames for you to choose from. If you
would like to use the random name generator in your program, put this program
in the same folder as your program, use the import "namegen" (case sensitive),
then use namegen.generate(count).

namegen.generate(count) returns a list of names, so you should probably save
the returned value to a variable.

https://github.com/BBaoVanC/NameGenerator
"""

# Imports
import os
import random
import urllib.request
import logging
import sys


# this is the url of the noun list
nouns_url = "https://f002.backblazeb2.com/file/bbaovanc-share/desiquintans.com_nounlist.txt"
# if the list doesn't exist
if not os.path.isfile("desiquintans.com_nounlist.txt"):
    # download the noun list
    urllib.request.urlretrieve(nouns_url, "desiquintans.com_nounlist.txt")


class ArgError(Exception):
    pass


def generate(count=1, debug=False):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open("desiquintans.com_nounlist.txt") as f:  # open the word list file
        words = f.readlines()  # read all lines into a list
    words = [x.strip() for x in words]  # remove the "\n" from each word
    wsuffixes = ["ator", "man", "guy", "ifier", "anator", ""]  # suffixes
    wprefixes = ["Mr", "The", ""]  # prefixes
    names = list()  # initialize the names list variable

    # vowels = ['a', 'e', 'i', 'o', 'u']
    # vowels2 = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels3 = ['a', 'i', 'o', 'u', 'y']
    n = 1
    while count >= n:
        word_pre = random.choice(words)  # choose a random word
        word_pre = word_pre.capitalize()  # capitalize the first letter
        wprefix = random.choice(wprefixes)  # choose a random prefix
        wsuffix = random.choice(wsuffixes)  # choose a random suffix
        wsuffix2 = wsuffix
        if wsuffix == "ator" or wsuffix == "anator":
            if random.choice([True, False, False]):
                wsuffix2 = wsuffix + "ifier"  # add the extra suffix of "ifier"

        # if we should make the name all caps
        caps = random.choice([True, False, False, False])
        if caps:  # if we are going to make it all caps
            wprefix = wprefix.upper()  # set the prefix to all caps
            word_pre = word_pre.upper()  # set the word to all caps
            wsuffix2 = wsuffix2.upper()  # set the suffix to all caps
            if len(wprefix) > 0:  # if there is a prefix
                wprefix = wprefix + "_"  # underscore at the end of the prefix

        if word_pre[-1] in vowels3:  # if the word ends in a vowel (aeiouy)
            if wsuffix == 'ator' or wsuffix == 'anator':  # grammar fix
                wsuffix = 'nator'  # set the suffix to "nator"

        # create a string 'word' which adds the 3 parts together
        word = str(wprefix) + str(word_pre) + str(wsuffix2)
        # choose if there should be a space before the number at the end
        space = random.choice(["_", "", ""])
        # choose a random number to have at the end
        number = random.randint(0, 999)
        # puts together the different parts of the username
        name = str(word) + str(space) + str(number)
        logging.debug("Generated name: " + name)
        names.append(name)  # add name to list of generated names
        n = n + 1  # increases our loop counter

    return names  # return the generated names


if __name__ == '__main__':  # if the program wasn't run as an import
    cmdline = sys.argv[1:]
    args = {"amt": 100,
            "debug": False,
            "file": "names.txt"
            }
    for arg in cmdline:
        if arg.startswith("amt="):
            args["amt"] = int(arg.split("=")[1])
        elif arg.startswith("debug="):
            b = arg.split("=")[1].capitalize()
            if b == "True":
                logging.basicConfig(level=logging.DEBUG)
            elif b == "False":
                logging.basicConfig(level=logging.INFO)
            else:
                raise(ArgError("Arg for 'debug' was neither True nor false"))
        elif arg.startswith("file="):
            args["file"] = str(arg.split("=")[1])
    logging.debug("Generating names")
    # use our function to generate 100 names into the variable usernames
    usernames = generate(count=args["amt"])
    logging.debug("Opening file")
    # open the list of names. + means to create the file if it doesn't exist
    file = open(args["file"], "w+")

    usernames2 = list()  # create new list named usernames2
    for item in usernames:
        # add newline character to each item in the usernames2 list...
        item = item + "\n"
        usernames2.append(item)  # ...
    usernames2[-1] = usernames2[-1].strip()  # remove newline from last item
    for item in usernames2:
        file.write(item)  # write each username to the file
        logging.debug("Writing name: " + item)
    logging.debug("Saving file")
    file.close()  # close the file and apply our changes
    logging.debug("Finished!")
