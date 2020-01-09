import numpy as np
import pandas as pd
from tqdm import tqdm
import warnings


tqdm.pandas(leave=False)
warnings.simplefilter("ignore", RuntimeWarning)

X = pd.read_csv("X300.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
eng = X.loc["England"]
cos = X.progress_apply(lambda x: np.dot(eng, x) / (np.linalg.norm(eng) * np.linalg.norm(x)), axis=1
        ).fillna(-1).sort_values(ascending=False)
print(cos[1:11])

