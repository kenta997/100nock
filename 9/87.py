import numpy as np
import pandas as pd


X = pd.read_csv("X300.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
v1 = X.loc["United_States"].values
v2 = X.loc["U.S"]

print(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

