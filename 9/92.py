import numpy as np
import pandas as pd
from gensim.models import word2vec
from tqdm import tqdm
import warnings


warnings.simplefilter("ignore", RuntimeWarning)

with open("91.txt", mode="r") as f:
    family = [x.strip().split(" ") for x in f.read().strip().split("\n")]

for csv_path, out_path in zip(["../8/X300.csv", "X300.csv"], ["92_85.txt", "92_90.txt"]):
    X = pd.read_csv(csv_path, header=None, index_col=0, quoting=2, keep_default_na=False)
    tqdm.pandas(desc="evaluate vector", leave=False)
    V = pd.DataFrame([x[:3] for x in family], columns=[0, 1, 2]).progress_apply(
            lambda x: (X.loc[x[1]] if x[1] in X.index else np.full(X.shape[1], np.nan)) -\
                    (X.loc[x[0]] if x[0] in X.index else np.full(X.shape[1], np.nan)) +\
                    (X.loc[x[2]] if x[2] in X.index else np.full(X.shape[1], np.nan)), axis=1)
    tqdm.pandas(desc="evaluate X norm", leave=False)
    cos = np.dot(V, X.T) / pd.concat([dv * X.progress_apply(np.linalg.norm, axis=1)
        for dv in tqdm(V.apply(np.linalg.norm, axis=1), desc="accumulate norm", leave=False)])
    similar = pd.concat([cos.idxmax(axis=1).fillna(""), cos.max(axis=1)]).values
    with open(out_path, mode="w") as f:
        for row, add in zip(tqdm(family, desc="write", leave=False), similar):
            f.write(" ".join(row + add.tolist()) + "\n")
#    with open(out_path, mode="w") as f:
#        for i, words in enumerate(tqdm(family, leave=False)):
#            try:
#                v = X.loc[words[1]] - X.loc[words[0]] + X.loc[words[2]]
#                cos = X.progress_apply(
#                        lambda x: np.dot(v, x) / (np.linalg.norm(v) * np.linalg.norm(x)), axis=1).fillna(-1)
#                similar = [cos.idxmax(), str(cos.max())]
#            except KeyError as e:
#                similar = ["", "-1"]
#            f.write(" ".join(words + [cos.idxmax(), str(cos.max())]) + "\n")

