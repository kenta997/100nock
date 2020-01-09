import numpy as np
import pandas as pd
from tqdm import tqdm


tqdm.pandas(leave=False)

X = pd.read_csv("X300.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
v = X.loc["Spain"] - X.loc["Madrid"] + X.loc["Athens"]
cos = X.progress_apply(lambda x: np.dot(v, x) / (np.linalg.norm(v) * np.linalg.norm(x)), axis=1
        ).fillna(-1).sort_values(ascending=False)
print(cos[:10])

