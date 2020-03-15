#!/usr/bin/env python3
"""
[methodname] Generator.

by [your GitHub username or other identifier]

[description]

Examples:
    [example 1]
    [example 2]
    [example 3]
"""

# Place your imports here.
import os
# ^^^ this is only necessary if you use this module, or if you require a
#     file as seen below.

# the following two lines of code are not required since they are only for
# requiring a file.
if not os.path.isfile("libnamegen/[requiredfile]"):
    print("ERROR: [requiredfile] could not be found!")


# Generation method
def gen(count=1, debug=False):  # you may add more arguments after debug
    """
    Generate names with the [methodname] method.

    Arguments:
    count -- the amount of names to generate (default 1)
    debug -- whether debug should be printed (default False)
    """
    with open("libnamegen/[requiredfile]") as f:  # use this block to read all
        # the data in your file
        words = f.readlines()  # read the file
    words = [x.strip() for x in words]  # remove newlines, now each line in
    # your file is an item in the list 'words'

    names = list()  # prepare the name list
    n = 1  # prepare loop counter

    while count >= n:
        name = "generated_name"  # this should generate a name and save it in
        # a variable named 'name'
        if debug:  # if we should output debug information
            print("Generated name: ({}/{})".format(n-1, count),
                  end="\r")  # log message for generated names
        names.append(name)  # add name to list
        n = n + 1  # increase counter

    if debug:  # if we should output debug information
        print("Generated name: ({}/{})...done".format(n-1, count))  # log msg
    return names  # return the names list
