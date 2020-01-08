import numpy as np
import pandas as pd
from scipy import sparse, io
from tqdm import tqdm

tc = pd.read_csv(
        "co_occurrence.csv", delimiter="\t", header=None, names=["tc", "count"], quoting=1, keep_default_na=False
        ).set_index("tc")["count"]
t = pd.read_csv(
        "count_t.csv", delimiter="\t", header=None, names=["t", "count"], quoting=1, keep_default_na=False
        ).set_index("t")["count"]
c = pd.read_csv(
        "count_c.csv", delimiter="\t", header=None, names=["c", "count"], quoting=1, keep_default_na=False
        ).set_index("c")["count"]
N = sum(tc)

X = sparse.lil_matrix((len(t.index), len(c.index)))
for pair, count in tqdm(tc.iteritems(), leave=False):
    index, column = (x for x in pair.split())
    X[t.index.get_loc(index), c.index.get_loc(column)] = max(
        [np.log((N * count) / (t[index] * c[column])), 0]) if count >= 10 else 0

io.savemat("X.mat", {"X": X})
