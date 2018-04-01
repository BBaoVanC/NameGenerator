# NameGenerator

[![Travis](https://img.shields.io/travis/BBaoVanC/NameGenerator.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Github All Releases](https://img.shields.io/github/downloads/BBaoVanC/NameGenerator/total.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator)
[![Codacy grade](https://img.shields.io/codacy/grade/58132ef8dc1d4d29b25d43a0ceb9b181.svg?style=flat-square)](https://github.com/BBaoVanC/NameGenerator)



Robust name generator that generates awesome names!

### Features:
  * Easy to use
  * Can be imported as a module
  * Only one function when imported as a module
  * Can be run directly as a standalone program
  * Always tested before release

---
### Examples:


Use defaults (one name and debug disabled):
```python
import namegen

# this uses the defaults which are one name and debug disabled
print(namegen.generate())
```
Prompt the user for the amount of names and enable debug:
```python
import namegen

amt = input("Amount of names to generate >> ")
count = int(amt)

names = namegen.generate(count, true)
for name in names:
  print(name)
```
---
### License
This is licensed under the MIT license. For more information, please refer to [`LICENSE.txt`](https://github.com/BBaoVanC/NNameGenerator/blob/master/LICENSE.txt)
