#!/usr/bin/python3
"""
Random Username Generator

by BBaoVanC

Documentation is located at:
https://github.com/BBaoVanC/NameGenerator
"""

# Imports
import logging
import sys


class ArgError(Exception):
    pass


helptxt = """Usage:
    python namegen.py [options]
Options:
    amt: Amount of names to generate
    debug: Whether or not to output debug information
    method: Which name generation method to use
Example:
    python namegen.py amt=50 debug=True file=mynames.txt method=classic"""
cmdline = sys.argv[1:]  # save arguments in varible 'cmdline'
args = {"amt": 100,
        "debug": False,
        "file": "names.txt",
        "method": "WILL BE SELECTED"
        }  # set default arguments
msel = False  # saves if the method has been selected
gennames = True  # saves if names should be generated
for arg in cmdline:  # this block converts 'cmdline' to dictionary 'args'
    if arg in ["--help", "-h", "help"]:
        print(helptxt)
        gennames = False
        args = {}

    elif arg.startswith("amt="):  # if the selected argument is 'amt'
        args["amt"] = int(arg.split("=")[1])  # save the selected amount

    elif arg.startswith("debug="):  # if the selected argument is 'debug'
        b = arg.split("=")[1].capitalize()  # capitalize the argument
        if b == "True":  # if the argument is true
            logging.basicConfig(level=logging.DEBUG)  # enable debug mode
            args["debug"] = True  # save this in argument list
        elif b == "False":  # if the argument is false
            logging.basicConfig(level=logging.INFO)  # disable debug mode
            args["debug"] = False  # save this in argument list
        else:  # if argument is neither True nor False
            raise(ArgError("Arg for 'debug' was neither True nor false"))

    elif arg.startswith("file="):  # if the selected argument is 'file'
        args["file"] = str(arg.split("=")[1])  # save this in argument list

    elif arg.startswith("method="):  # if the selected argument is 'method'
        msel = True
        b = arg.split("=")[1].lower()  # convert argument to lowercase
        if b == "classic":  # if method is 'classic'
            from generators import classic
            args["method"] = classic  # save this in argument list
        elif b == "v2":  # if method is 'v2'
            from generators import v2
            args["method"] = v2  # save this in argument list
        elif b == "random":
            from generators import random  # if method is the random gen
            args["method"] = random  # save this in argument list
        else:
            raise(ArgError("Arg for 'method' is invalid"))

if gennames == True:
    if not msel:
        from generators import classic
        args["method"] = classic
    logging.debug("Generating names")
    # use our function to generate names into the variable 'usernames'
    usernames = args["method"].gen(count=args["amt"], debug=args["debug"])
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
        logging.debug("Writing name: " + item.strip("\n"))
    logging.debug("Saving file")
    file.close()  # close the file and apply our changes
    logging.debug("Finished!")
