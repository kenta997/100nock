import numpy as np
import pandas as pd
from gensim.models import word2vec
from tqdm import tqdm
import warnings
from processing import ProcessThread 


warnings.simplefilter("ignore", RuntimeWarning)
process = ProcessThread()

with open("91.txt", mode="r") as f:
    family = [x.strip().split(" ") for x in f.read().strip().split("\n")]

for csv_path, out_path in zip(["../8/X300.csv", "X300.csv"], ["92_85.txt", "92_90.txt"]):
    X = pd.read_csv(csv_path, header=None, index_col=0, quoting=2, keep_default_na=False)

    tqdm.pandas(desc="evaluate vector", leave=False)
    V = pd.DataFrame([x[:3] for x in family], columns=[0, 1, 2]).progress_apply(
            lambda x: (X.loc[x[1]] if x[1] in X.index else np.full(X.shape[1], np.nan)) -\
                    (X.loc[x[0]] if x[0] in X.index else np.full(X.shape[1], np.nan)) +\
                    (X.loc[x[2]] if x[2] in X.index else np.full(X.shape[1], np.nan)), axis=1)

    tqdm.pandas(desc="evaluate V norm", leave=False)
    dv = V.progress_apply(np.linalg.norm, axis=1)

    tqdm.pandas(desc="evaluate X norm", leave=False)
    dx = X.progress_apply(np.linalg.norm, axis=1)

    print("evaluate cos ...", end="  ")
    process.start()
    cos = pd.DataFrame(
            np.dot(V, X.T) / np.dot(dv.values.reshape(-1, 1), dx.values.reshape(1, -1)), index=V.index, columns=X.index)
    process.done()

    similar = pd.concat([cos.idxmax(axis=1).fillna(""), cos.max(axis=1).fillna(-1)], axis=1).astype(str).values

    with open(out_path, mode="w") as f:
        for row, add in zip(tqdm(family, desc="write", leave=False), similar):
            f.write(" ".join(row + add.tolist()) + "\n")

