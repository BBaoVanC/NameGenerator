# NameGenerator

This is a name generator that I wrote which can generate some pretty silly
names!

### Features:
  * Can be imported as a module
  * Only one function when imported as a module
  * Can be run directly as a standalone program
  * Easy to use

---
### Examples:


Use defaults (one name and debug disabled):
```python
import namegen

# this uses the defaults which are one name and debug off
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
