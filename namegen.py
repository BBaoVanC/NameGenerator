"""
Random Username Generator

by BBaoVanC

Generates a file with 100 different usernames for you to choose from. If you
would like to use the random name generator in your program, put this program
in the same folder as your program, use the import "namegen" (case sensitive),
then use namegen.generate(count).

namegen.generate(count) returns a list of names, so you should probably save
the returned value to a variable.
"""

# Imports
import os
import random
import urllib.request


# this is the url of the noun list
nouns_url = "http://benstar.wc.lt/random_files/desiquintans.com_nounlist.txt"
# if the list doesn't exist
if not os.path.isfile("desiquintans.com_nounlist.txt"):
    # download the noun list
    urllib.request.urlretrieve(nouns_url, "desiquintans.com_nounlist.txt")


def generate(count, debug):
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
        if debug:  # if debug mode is enabled
            print("Generated name: " + name)
        names.append(name)  # add name to list of generated names
        n = n + 1  # increases our loop counter

    return names  # return the generated names


if __name__ == '__main__':  # if the program wasn't run as an import
    print("Generating names")
    # use our function to generate 100 names into the variable usernames
    usernames = generate(100, True)
    print("Opening file")
    # open the list of names. + means to create the file if it doesn't exist
    file = open("names.txt", "w+")

    usernames2 = list()  # create new list named usernames2
    for item in usernames:
        # add newline character to each item in the usernames2 list...
        item = item + "\n"
        usernames2.append(item)  # ...
    usernames2[-1] = usernames2[-1].strip()  # remove newline from last item
    for item in usernames2:
        file.write(item)  # write each username to the file
        # print("Writing name: " + item)

    # ================================UNOPTIMIZED ALGORITHM================== #
    # usernames2 = list()  # create new empty list named usernames2           #
    # for item in usernames:                                                  #
    #     item = item + "\n"  # add a newline to the end of each name         #
    #     usernames2.append(item)                                             #
    # lastname = usernames2[-1]  # set variable lastname to the last name     #
    # lastname = lastname.strip()  # remove newline character from lastname   #
    # usernames2 = usernames2[:-1]  # remove last item from usernames2        #
    # usernames2.append(lastname)  # add lastname to usernames2               #
    #                                                                         #
    # for username in usernames2:  # for each username                        #
    #     file.write(username)  # write username to the file                  #
    # ================================UNOPTIMIZED ALGORITHM================== #

    print("Saving file")
    file.close()  # close the file and apply our changes
    print("Finished!")
