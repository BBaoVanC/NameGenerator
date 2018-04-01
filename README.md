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
