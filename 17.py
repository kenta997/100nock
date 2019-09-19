import sys

s = set([x.split()[0] + "\n" for x in sys.stdin.readlines()])
print(len(s))
print("".join(sorted(list(s))))

