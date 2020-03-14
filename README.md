# NameGenerator

[![AWESOMENESS](https://img.shields.io/badge/awesomeness-maximum-00a0af.svg)](https://www.youtube.com/channel/UCCiDxF_RZ4fTU_gGJRz-fwQ)
[![Build Status](https://travis-ci.org/BBaoVanC/NameGenerator.svg?branch=master)](https://travis-ci.org/BBaoVanC/NameGenerator)
[![license](https://img.shields.io/github/license/BBaoVanC/NameGenerator.svg)](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
[![Github All Releases](https://img.shields.io/github/downloads/BBaoVanC/NameGenerator/total.svg)](https://github.com/BBaoVanC/NameGenerator)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6621a967fffe47069d53b19129b7be0c)](https://www.codacy.com/manual/BBaoVanC/NameGenerator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BBaoVanC/NameGenerator&amp;utm_campaign=Badge_Grade)
[![GitHub watchers](https://img.shields.io/github/watchers/BBaoVanC/NameGenerator.svg?label=Watch)](https://github.com/BBaoVanC/NameGenerator)
[![GitHub stars](https://img.shields.io/github/stars/BBaoVanC/NameGenerator.svg?label=Stars)](https://github.com/BBaoVanC/NameGenerator)

[![GitHub issues](https://img.shields.io/github/issues-raw/BBaoVanC/NameGenerator.svg)](https://github.com/BBaoVanC/NameGenerator/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/BBaoVanC/NameGenerator.svg)](https://github.com/BBaoVanC/NameGenerator/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed)

Robust name generator that generates awesome names!

## Features

* Easy to use
* CLI with simple arguments
* Can be imported as a module
* Only one function when imported as a module
* Can be run directly as a standalone program
* Two types of names to generate
* Always tested before release
* Uses Python 3
* Supports latest 3 versions of Python

---

## How to Download

To download the latest stable version of NameGenerator, click the green button labeled `Clone or download`. Then, click `Download ZIP` to download a ZIP archive containing all of the files. Then, extract the archive.

![Clone or download button](https://i.imgur.com/1SHfJzR.png)

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

To use the command-line interface, you must have namegen.py and the generators folder. If you will only use specific generators, you don't need to download the other unused ones.

Please note that this program is written for Python 3.

If you use Windows, use the command `py` instead of `python`. If you have both Python 2 and Python 3 installed, use `py -3`.

If you use Mac/Linux, and have both Python 2 and Python 3 installed, then use the command `python3`.

Use defaults (100 names, debug enabled, classic method, write names to names.txt):

``` plaintext
$ python namegen.py
Generating names...
[####################] 100%...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100%...done
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
[####################] 100%...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100%...done
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
[####################] 100%...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100%...done
Saving file...
Finished!
```

Generate names and place in file users.txt inside the directory "example-names" **(Directory must already exist!)**

``` plaintext
$ python namegen.py file=example-names/users.txt
Generating names...
[####################] 100%...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100%...done
Saving file...
Finished!
```

Generate 50 names with debug enabled and place in namelist.txt:

``` plaintext
$ python namegen.py amt=50 debug=True file=namelist.txt
Generating names...
[####################] 100%...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100%...done
Saving file...
Finished!
```

The default name generation method is classic, and looks like 'TheAssignmentanatorifier_90'.

The generation method random looks like 'XaYyaknkCoH8'.

You can change the generation method used by using the argument 'method=[method]' and replace [method] with the correct method.

``` plaintext
$ python namegen.py method=classic
Generating names...
[####################] 100%...done
Preparing list to write to file...done
Opening file...
Writing names...
[####################] 100%...done
Saving file...
Finished!
```

Double-clicking namegen.py will generate using default options.

---

### API

To use the API, you only need the generators folder.

Generate one classic name without debug:

``` python
from generators import classic

# this uses the defaults which are one name, debug disabled, and classic generator
print(classic.gen())
```

Generate seven classic names with debug:

``` python
from generators import classic

print(classic.gen(count=7, debug=True))
# print(classic.gen(7, True))  # also valid
```

Prompt the user for the amount of names, enable debug, and generate classic names:

``` python
from generators import classic

amt = input("Amount of names to generate >> ")
count = int(amt)

names = classic.gen(count, true)
for name in names:
  print(name)
```

Generate one random name without debug:

``` python
from generators import random

print(random.gen())
```

Generate one name using the random method 15 characters long:

``` python
from generators import random

print(random.gen(length=15))
```

---

## License

_NameGenerator_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE.txt`](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
