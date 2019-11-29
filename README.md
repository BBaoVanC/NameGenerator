# NameGenerator

[![AWESOMENESS](https://img.shields.io/badge/awesomeness-maximum-00a0af.svg?style=flat-square)](https://www.youtube.com/channel/UCCiDxF_RZ4fTU_gGJRz-fwQ)
[![Travis](https://img.shields.io/travis/BBaoVanC/NameGenerator.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator)
[![license](https://img.shields.io/github/license/BBaoVanC/NameGenerator.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
[![Github All Releases](https://img.shields.io/github/downloads/BBaoVanC/NameGenerator/total.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator)
[![Codacy grade](https://img.shields.io/codacy/grade/58132ef8dc1d4d29b25d43a0ceb9b181.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator)
[![GitHub watchers](https://img.shields.io/github/watchers/BBaoVanC/NameGenerator.svg?style=flat-square&label=Watch)](https://github.com/BBaoVanC/NameGenerator)
[![GitHub stars](https://img.shields.io/github/stars/BBaoVanC/NameGenerator.svg?style=flat-square&label=Stars)](https://github.com/BBaoVanC/NameGenerator)

[![GitHub issues](https://img.shields.io/github/issues-raw/BBaoVanC/NameGenerator.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/BBaoVanC/NameGenerator.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed)

Robust name generator that generates awesome names!

### Features:
  * Easy to use
  * Useful command-line arguments
  * Can be imported as a module
  * Only one function when imported as a module
  * Can be run directly as a standalone program
  * Three types of names to generate
  * Always tested before release
  * Uses Python 3
  * Supports latest 3 versions of Python

---
### Command-Line Examples:


To use the command-line or double-click launch, you must have namegen.py and the generators folder. If you only use specific generators, you don't need to download the other unused ones.

Please note that this program is written for Python 3. It might work in Python 2, but there is no guarantee. If you have both Python 2 and 3 installed, use the command `python3` instead of `python`

Use defaults (100 names, debug disabled, write names to names.txt):
```
python namegen.py
```
Show help menu (use any of the three options in brackets):
```
python namegen.py [--help | -h | help]
```
Generate 250 names:
```
python namegen.py amt=250
```
Generate default amount of names with debug enabled:
```
python namegen.py debug=True
```
Generate names and place in file usernames.txt:
```
python namegen.py file=usernames.txt
```
Generate names and place in file users.txt inside the directory "example-names" **(Directory must already exist!)**
```
python namegen.py file=example-names/users.txt
```
Generate 50 names with debug enabled and place in namelist.txt:
```
python namegen.py amt=50 debug=True file=namelist.txt
```
The default name generation method is classic, and looks like 'TheAssignmentanatorifier_90'.

The generation method random looks like 'XaYyaknkCoH8'.

You can change the generation method used by using the argument 'method=[method]' and replace [method] with the correct method.
```
python namegen.py method=classic
```
Double-clicking namegen.py will generate 100 names with debug disabled and the classic method into names.txt.

---
### API Examples:


To use the API, you only need the generators folder.

Generate classic name:
```python
from generators import classic

# this uses the defaults which are one name, debug disabled, and class
print(classic.gen())
```
Prompt the user for the amount of names, enable debug, and generate classic names:
```python
from generators import classic

amt = input("Amount of names to generate >> ")
count = int(amt)

names = classic.gen(count, true)
for name in names:
  print(name)
```
Generate one name using the random method:
```python
from generators import random

print(random.gen())
```
Generate one name using the random method 15 characters long:
```python
from generators import random

print(random.gen(length=15))
```

---
### License
_NameGenerator_ is licensed under the MIT license. For more information, please refer to [`LICENSE.txt`](https://github.com/BBaoVanC/NameGenerator/blob/master/LICENSE.txt)
