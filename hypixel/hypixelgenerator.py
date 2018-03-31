import random


def generate(count):
    with open("words.txt") as f:
        words = f.readlines()
    words = [x.strip() for x in words]
    names = list()

    n = 1
    while n <= count:
        word = random.choice(words)
        space = random.choice(["_", "__", ""])
        number = random.randint(0, 99)
        name = str(word) + str(space) + str(number)
        names.append(name)
        n = n + 1
    return names


file = open("names.txt", "w+")
usernames = generate(100)
for username in usernames:
    file.write(username + "\n")
file.close()
