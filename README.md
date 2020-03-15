# NameGenerator

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6621a967fffe47069d53b19129b7be0c)](https://www.codacy.com/manual/BBaoVanC/NameGenerator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BBaoVanC/NameGenerator&amp;utm_campaign=Badge_Grade)
[![Travis CI](https://travis-ci.org/BBaoVanC/NameGenerator.svg?branch=master)](https://travis-ci.org/BBaoVanC/NameGenerator)
[![CircleCI](https://circleci.com/gh/BBaoVanC/NameGenerator/tree/master.svg?style=svg)](https://circleci.com/gh/BBaoVanC/NameGenerator/tree/master)

[![license](https://img.shields.io/github/license/BBaoVanC/NameGenerator.svg)](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
[![Github All Releases](https://img.shields.io/github/downloads/BBaoVanC/NameGenerator/total.svg)](https://github.com/BBaoVanC/NameGenerator)
[![GitHub watchers](https://img.shields.io/github/watchers/BBaoVanC/NameGenerator.svg?label=Watch)](https://github.com/BBaoVanC/NameGenerator)
[![GitHub stars](https://img.shields.io/github/stars/BBaoVanC/NameGenerator.svg?label=Stars)](https://github.com/BBaoVanC/NameGenerator)

[![GitHub issues](https://img.shields.io/github/issues-raw/BBaoVanC/NameGenerator.svg)](https://github.com/BBaoVanC/NameGenerator/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/BBaoVanC/NameGenerator.svg)](https://github.com/BBaoVanC/NameGenerator/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed)

Robust name generator that generates awesome names!

## Features

* Easy to use
* CLI with simple arguments
* `libnamegen` can be imported as a module
* `libprogress` can be imported as a module
* CLI can be run with default settings by double-clicking
* Two generation methods to choose from
* Always tested before release
* Uses Python 3
* Supports latest 3 versions of Python

---

## How to Download

To download the latest stable version of NameGenerator, click the button labeled `Releases` above the file explorer.

![Releases button](https://i.imgur.com/EWNIpBn.png)

Then, under the release labeled `Latest release`, click the button labeled `Source Code (zip)` under `Assets`. Then extract the downloaded zip archive.

![Download button](https://i.imgur.com/PPqLAQu.png)

---

## FAQ

**I get an error when I run namegen.py or use the CLI.**

If you get this error (or similar):

``` python
  File "namegen.py", line 87
    print("Preparing list to write to file", end="\r")  # log message
                                                ^
SyntaxError: invalid syntax
```

Check your Python version. NameGenerator doesn't work on Python 2. It's also only *tested* on the latest 3 versions of Python 3. There is no guarantee that NameGenerator will work on earlier versions.

---

## Documentation

### Command-Line Interface

To use the command-line interface, you must have namegen.py and the `libnamegen` folder. If you will only use specific generators, you don't need to download the other unused ones.

Please note that this program is written for Python 3.

If you use Windows, use the command `py` instead of `python`. If you have both Python 2 and Python 3 installed, use `py -3`.

If you use Mac/Linux, and have both Python 2 and Python 3 installed, then use the command `python3`.

Use defaults (100 names, debug enabled, classic method, write names to names.txt):

``` plaintext
$ python namegen.py
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Show help menu (use any of the three options in brackets):

``` plaintext
$ python namegen.py [--help | -h | help]
Usage:
    python namegen.py [options]
Options:
    amt: Amount of names to generate
    debug: Whether or not to output debug information
    method: Which name generation method to use
Example:
    python namegen.py amt=50 debug=True file=mynames.txt method=classic
```

Generate 250 names:

``` plaintext
$ python namegen.py amt=250
Generating names...
[####################] 100% [250/250]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [250/250]...done
Saving file...
Finished!
```

Generate default amount of names with debug disabled:

``` plaintext
$ python namegen.py debug=False
(no output)
```

Generate names and place in file usernames.txt:

``` plaintext
$ python namegen.py file=usernames.txt
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Generate names and place in file users.txt inside the directory "example-names" **(Directory must already exist!)**

``` plaintext
$ python namegen.py file=example-names/users.txt
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Generate 50 names with debug enabled and place in namelist.txt:

``` plaintext
$ python namegen.py amt=50 debug=True file=namelist.txt
Generating names...
[####################] 100% [50/50]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [50/50]...done
Saving file...
Finished!
```

The default name generation method is classic, and looks like 'TheAssignmentanatorifier_90'.

The generation method random looks like 'XaYyaknkCoH8'.

You can change the generation method used by using the argument 'method=[method]' and replace [method] with the correct method.

``` plaintext
$ python namegen.py method=random
Generating names...
[####################] 100% [100/100]...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100% [100/100]...done
Saving file...
Finished!
```

Double-clicking namegen.py will generate using default options.

---

### API

To use the API, you only need the `libnamegen` folder.

Generate one classic name without debug:

``` python
from libnamegen import classic

# this uses the defaults which are one name, debug disabled, and classic generator
print(classic.gen())
```

Generate seven classic names with debug:

``` python
from libnamegen import classic

print(classic.gen(count=7, debug=True))
# print(classic.gen(7, True))  # also valid
```

Prompt the user for the amount of names, enable debug, and generate classic names:

``` python
from libnamegen import classic

amt = input("Amount of names to generate >> ")
count = int(amt)

names = classic.gen(count, true)
for name in names:
  print(name)
```

Generate one random name without debug:

``` python
from libnamegen import random

print(random.gen())
```

Generate one name using the random method 15 characters long:

``` python
from libnamegen import random

print(random.gen(length=15))
```

---

### Progress Bar API

To use the progress bar API, you only need the libprogress folder.

The following is an example that utilizes a progress bar with default length.

``` python
import libprogress

for i in range(20):
    do(something)
    print(libprogress.genbar(curprg=i+1, maxprg=20), end="\r")
print(libprogress.genfullbar(prg=20))
```

Final output:

``` plaintext
[####################] 100% [100/100]...done
```

If you don't put `end="\r"`, then each progress bar won't overwrite the last. The output will look like the following:

``` plaintext
[#-------------------] 5% [1/20]
[##------------------] 10% [2/20]
[###-----------------] 15% [3/20]
[####----------------] 20% [4/20]
[#####---------------] 25% [5/20]
[######--------------] 30% [6/20]
[#######-------------] 35% [7/20]
[########------------] 40% [8/20]
[#########-----------] 45% [9/20]
[##########----------] 50% [10/20]
[###########---------] 55% [11/20]
[############--------] 60% [12/20]
[#############-------] 65% [13/20]
[##############------] 70% [14/20]
[###############-----] 75% [15/20]
[################----] 80% [16/20]
[#################---] 85% [17/20]
[##################--] 90% [18/20]
[###################-] 95% [19/20]
[####################] 100% [20/20]
[####################] 100% [20/20]...done
```

---

## License

_NameGenerator_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE.txt`](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
