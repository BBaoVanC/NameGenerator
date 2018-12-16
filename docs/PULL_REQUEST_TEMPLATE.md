If you would like to make a pull request to add a new name generation method, please use the template below. The only edits you need to make are creating a file in the generators folder for your generation method. If I accept your pull request, I will manually add command-line and double click support in namegen.py. Replace [methodname] with the name of your generation method. The following code block is the template, also stored in **docs/gentemplate.py**. If you are writing a new generation method, copy this template and edit it. Comments in the template are meant for explaining the template; they may be removed. Please try to document everything using comments.

generators/[methodname].py
```python
"""
[methodname] Generator

by [your GitHub username or other identifier]

[description]

Examples:
    [example 1]
    [example 2]
    [example 3]
"""

# Place your imports here.
import os  # this is only necessary if you use this module, or if you require a
# file as seen below.
import logging

logging.basicConfig(level=logging.INFO)
# the following two lines of code are not required since they are only for
# requiring a file.
if not os.path.isfile("generators/[requiredfile]"):
    logging.critical("[requiredfile] could not be found!")


# Generation method
def gen(count=1, debug=False):  # you may add more arguments after debug
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open("generators/[requiredfile]") as f:  # use this block to read all
        # the data in your file
        words = f.readlines()  # read the file
    words = [x.strip() for x in words]  # remove newlines, now each line in
    # your file is an item in the list 'words'

    names = list()
    n = 1

    while count >= n:
        name = "generated_name"  # this should generate a name and save it in
        # a variable named 'name'
        logging.debug("Generated name: " + name)
        names.append(name)
        n = n + 1

    return names

```
