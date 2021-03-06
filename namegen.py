#!/usr/bin/env python3
"""
Random Username Generator.

by BBaoVanC

Documentation is located at:
https://github.com/BBaoVanC/NameGenerator

Copyright (C) 2020 BBaoVanC
"""

# Imports
import sys
import libprogress


class ArgError(Exception):  # custom error for invalid arguments
    """This error occurs when an argument passed to the program is invalid."""

    pass


helptxt = """Usage:
    python namegen.py [options]
Options:
    amt: Amount of names to generate
    debug: Whether or not to output debug information
    method: Which name generation method to use
Example:
    python namegen.py amt=50 debug=True file=mynames.txt method=classic"""
# ^^^ this is the help menu text ^^^ #

cmdline = sys.argv[1:]  # save arguments in varible 'cmdline'
args = {"amt": 100,  # default amount of names to generate
        "debug": True,  # enable debug by default
        "file": "names.txt",  # default file name
        "method": "WILL BE SELECTED"  # don't select the method yet
        }  # default arguments
msel = False  # saves if the method has been selected
gennames = True  # saves if names should be generated
for arg in cmdline:  # this block converts 'cmdline' to dictionary 'args'
    if arg in ["--help", "-h", "help"]:  # if one of the help options is used
        print(helptxt)  # print the help menu text
        gennames = False  # don't generate names
        break  # break out of the loop to prevent other args from being checked

    elif arg.startswith("amt="):  # if the selected argument is 'amt'
        args["amt"] = int(arg.split("=")[1])  # save the selected amount

    elif arg.startswith("debug="):  # if the selected argument is 'debug'
        b = arg.split("=")[1].capitalize()  # capitalize the argument
        if b == "True":  # if the argument is true
            args["debug"] = True  # save this in argument list
        elif b == "False":  # if the argument is false
            args["debug"] = False  # save this in argument list
        else:  # if argument is neither True nor False
            raise(ArgError("Arg for 'debug' was neither True nor false"))

    elif arg.startswith("file="):  # if the selected argument is 'file'
        args["file"] = str(arg.split("=")[1])  # save this in argument list

    elif arg.startswith("method="):  # if the selected argument is 'method'
        msel = True  # note that the method has been selected
        b = arg.split("=")[1].lower()  # convert argument to lowercase
        if b == "classic":  # if method is 'classic'
            from libnamegen import classic  # import the classic method
            args["method"] = classic  # save this in argument list
        elif b == "random":  # if method is 'random'
            from libnamegen import random  # if method is the random gen
            args["method"] = random  # save this in argument list
        else:  # if none of the existing methods was selected
            raise(ArgError("Arg for 'method' is invalid"))

if gennames is True:  # if we should generate the names
    if not msel:  # if the method hasn't been selected
        from libnamegen import classic  # import the classic method
        args["method"] = classic  # save the method in argument list
    if args["debug"]:  # if we should output debug information
        print("Generating names...")  # log message
    # use our function to generate names into the variable 'usernames'
    # pylint: disable=no-member
    usernames = args["method"].gen(count=args["amt"], debug=args["debug"])
    # ^^^ generate the names with the selected method and options ^^^ #

    if args["debug"]:  # if we should output debug information
        print("Preparing list to write to file", end="\r")  # log message

    # vvv prepare a list for writing directly to the file vvv #
    usernames2 = list()  # create new list named usernames2
    for item in usernames:  # for each item in the username list
        # add newline character to each item in the usernames2 list...
        item = item + "\n"  # add a newline to the end of each name
        usernames2.append(item)  # ...
    usernames2[-1] = usernames2[-1].strip()  # remove newline from last item
    if args["debug"]:  # if we should output debug information
        print("Preparing list to write to file...done")  # log message

    # vvv start making file vvv #
        print("Opening file...")
    # open the list of names. + means to create the file if it doesn't exist
    file = open(args["file"], "w+")  # open the file in overwrite mode (w+)

    wtotal = len(usernames2)  # save the total names in wtotal for progress log
    if args["debug"]:  # if debug is enabled
        print("Writing names...")
    for indx, item in enumerate(usernames2):  # indx is the index
        file.write(item)  # write each username to the file
        if args["debug"]:  # if we should output debug information
            print(libprogress.genbar(curprg=indx+1, maxprg=wtotal), end="\r")
            # ^^^ log message ^^^ #
    if args["debug"]:  # if we should output debug information
        print(libprogress.genfullbar(prg=wtotal))
        print("Saving file...")  # log message
    file.close()  # close the file and apply our changes
    if args["debug"]:  # if we should output debug information
        print("Finished!")  # log message
