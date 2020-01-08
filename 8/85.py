import numpy as np
import pandas as pd
import csv
from scipy import sparse, io
from sklearn.decomposition import TruncatedSVD
from processing import ProcessThread


thread = ProcessThread()

X = io.loadmat("X")["X"]

print("load index ...", end="  ")
thread.start()
index = pd.read_csv("count_t.csv",
        delimiter="\t",
        header=None,
        names=["t", "count"],
        usecols=["t"],
        quoting=1,
        keep_default_na=False)["t"]
thread.done()

print("pca ...", end="  ")
thread.start()
pca = TruncatedSVD(300)
X = pd.DataFrame(pca.fit_transform(X), index=index)
thread.done()

print("to csv ...", end="  ")
thread.start()
X.to_csv("X300.csv", header=False, quoting=csv.QUOTE_NONNUMERIC)
thread.done()

