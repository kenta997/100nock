import sys
import collections
import numpy as np

col1 = [x.split()[0] for x in sys.stdin.readlines()]
c = collections.Counter(col1)
value_counts = np.hstack([np.array(list(c.values())).reshape(-1, 1), np.array(list(c.keys())).reshape(-1, 1)])
value_counts = value_counts[np.argsort(value_counts[:, 0])[::-1]]
print("\n".join(["\t".join(x) for x in value_counts]))

