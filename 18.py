import sys
import numpy as np

s = np.array([x.split() for x in sys.stdin.readlines()])
s = s[np.argsort(s[:, 2], axis=0)[::-1]]
print("".join(["\t".join(x) +"\n" for x in s]))

