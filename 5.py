
filepath = "hash.txt"
with open(filepath) as fp:
    chars = fp.read()
with open(filepath, "w") as fp:
    for char in chars:
        print(char + "#",end="", file=fp)
