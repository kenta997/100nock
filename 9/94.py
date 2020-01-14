import os
from subprocess import call
import numpy as np
import pandas as pd
import csv
from tqdm import tqdm
from download import download


if not os.path.exists("wordsim353/combined.csv"):
    download("http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/wordsim353.zip", "wordsim353.zip", True)
    call(["mkdir", "wordsim353"])
    call(["unzip", "wordsim353.zip", "-d", "wordsim353"])

df = pd.read_csv("wordsim353/combined.csv")

for x_path, out_path in zip(["../8/X300.csv", "X300.csv"], ["94_85.csv", "94_90.csv"]):
    X = pd.read_csv(x_path, header=None, index_col=0, keep_default_na=False)

    get_vector = lambda word: X.loc[word] if word in X.index else np.full(X.shape[1], np.nan)
    
    V1 = df["Word 1"].apply(get_vector)
    V2 = df["Word 2"].apply(get_vector)
    
    cos = (V1.values * V2.values).sum(axis=1) /\
            (V1.apply(np.linalg.norm, axis=1) * V2.apply(np.linalg.norm, axis=1))

    df.assign(cos=cos).to_csv(out_path, index=False)

