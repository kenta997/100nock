import sys

s = sys.stdin.readlines()
n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
print("".join(s[-n:]))

