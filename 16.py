import sys
import numpy as np

s = np.array(sys.stdin.readlines())
n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
for x in np.array_split(s, n):
    print("".join(x))

