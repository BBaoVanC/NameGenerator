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
### Credit Requirements:
  1. Include *https://github.com/BBaoVanC/NameGenerator* in your credits and as a comment at the beginning of each program which uses it.
  2. Do not use this program as your own work.
  3. If you make edits to it, make sure to keep the link to the Github repository in the block comment at the beginning.
  4. Remember that you can always send your edited version to me by forking the project and sending a pull request!
