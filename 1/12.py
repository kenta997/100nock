import sys

s = sys.stdin.readlines()
with open("col1.txt", mode="w") as f:
    f.write("".join([x.split()[0] + "\n" for x in s]))

with open("col2.txt", mode="w") as f:
    f.write("".join([x.split()[1] + "\n" for x in s]))

