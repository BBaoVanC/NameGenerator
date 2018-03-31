"""
Random Username Generator

by BBaoVanC

Generates a file with 100 different usernames for you to choose from. If you would like to use the random name
generator in your program, put this program in the same folder as your program, use the import "namegen"
(case sensitive), then use namegen.generate(count)
Returns a list of names, so you should probably save a variable to namegen.generate(count)
"""

import os
import random
import urllib.request

if not os.path.isfile("desiquintans.com_nounlist.txt"):
    urllib.request.urlretrieve("http://benstar.wc.lt/random_files/desiquintans.com_nounlist.txt",
                               "desiquintans.com_nounlist.txt")


def generate(count, debug):
    with open("desiquintans.com_nounlist.txt") as f:  # open the word list file
        words = f.readlines()  # read all lines into a list
    words = [x.strip() for x in words]  # remove the "\n" from each word
    names = []
    for i in range(count):
        ntype = random.choice(["1", "2"])
        if ntype == "1":
            wsuffixes = ["ator", "man", "guy", "ifier", "anator", ""]  # create a list of suffixes we can use
            wprefixes = ["Mr", "The", ""]  # create a list of prefixes we can use
            names = list()  # create blank list of generated names

            # vowels = ['a', 'e', 'i', 'o', 'u']
            # vowels2 = ['a', 'e', 'i', 'o', 'u', 'y']
            vowels3 = ['a', 'i', 'o', 'u', 'y']
            word_pre = random.choice(words)  # choose a random word from the list of words
            word_pre = word_pre.capitalize()
            wprefix = random.choice(wprefixes)  # choose a random prefix from the list
            wsuffix = random.choice(wsuffixes)  # choose a random suffix from the list
            wsuffix2 = wsuffix
            if wsuffix == "ator" or wsuffix == "anator":
                if random.choice([True, False, False]):
                    wsuffix2 = wsuffix + "ifier"

            caps = random.choice([True, False, False, False])  # if we should make the name all caps
            if caps:  # if we are going to make it all caps
                wprefix = wprefix.upper()  # set the prefix to all caps
                word_pre = word_pre.upper()  # set the word to all caps
                wsuffix2 = wsuffix2.upper()  # set the suffix to all caps
                if len(wprefix) > 0:  # if there is a prefix
                    wprefix = wprefix + "_"  # add an underscore to the end of the prefix

            if word_pre[-1] in vowels3:  # if the word ends in a vowel (including 'y')
                if wsuffix == 'ator' or wsuffix == 'anator':  # if the randomly chosen suffix is "ator" or "anator"
                    wsuffix = 'nator'  # set the suffix to "nator"

            word = str(wprefix) + str(word_pre) + str(wsuffix2)  # create string 'word' which adds the 3 parts together
            space = random.choice(["_", "", ""])  # choose if there should be a space before the number at the end
            number = random.randint(0, 999)  # choose a random number to have at the end
            name = str(word) + str(space) + str(number)  # puts together the different parts of the username
            if debug:
                print("Generated name: " + name)
            names.append(name)  # add name to list of generated names

        elif ntype == "2":

            if random.choice([True, False]):
                suffix = random.randint(0, 999)
            else:
                suffix = ""
            name = str(random.choice(words)).capitalize() + str(random.choice(words)).capitalize() + \
                   str(random.choice(words)).capitalize() + str(suffix)
            names.append(name)

    return names  # return the generated names


if __name__ == '__main__':  # if the program was not run as an import
    print("Generating names")
    usernames = generate(100, True)  # use our function to generate 100 names into the variable usernames
    print("Opening file")
    file = open("names.txt", "w+")  # open the list of names. + means to create the file if it doesn't exist

    usernames2 = list()  # create new list named usernames2
    for item in usernames:
        item = item + "\n"  # add newline character to each item in the usernames2 list...
        usernames2.append(item)  # ...
    usernames2[-1] = usernames2[-1].strip()  # remove newline character from last item in list
    for item in usernames2:
        file.write(item)  # write each username to the file
        # print("Writing name: " + item)

    # ================================UNOPTIMIZED ALGORITHM================================ #
    # usernames2 = list()  # create new empty list named usernames2                         #
    # for item in usernames:                                                                #
    #     item = item + "\n"  # add a newline character to the end of each username         #
    #     usernames2.append(item)                                                           #
    # lastname = usernames2[-1]  # set variable lastname to the last name in usernames2     #
    # lastname = lastname.strip()  # remove newline character from lastname                 #
    # usernames2 = usernames2[:-1]  # remove last item from usernames2                      #
    # usernames2.append(lastname)  # add lastname to usernames2                             #
    #                                                                                       #
    # for username in usernames2:  # for each username in the list of usernames             #
    #     file.write(username)  # write username to file along with a newline character     #
    # ================================UNOPTIMIZED ALGORITHM================================ #

    print("Saving file")
    file.close()  # close the file so other programs can access it and apply our changes
    print("Finished!")
