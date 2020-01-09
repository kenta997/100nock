import numpy as np
import pandas as pd


X = pd.read_csv("X300.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
eng = X.loc["England"]
cos = X.T.apply(lambda x: np.dot(eng, x) / (np.linalg.norm(eng) * np.linalg.norm(x))
        ).T.fillna(-1).sort_values(ascending=False)
print(cos[1:11])

