import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


X = pd.read_csv("X300_country.csv", header=None, index_col=0, quoting=2, keep_default_na=False)

model = KMeans(n_clusters=5, random_state=1)
model.fit(X)
X["cluster"] = model.labels_

print(X["cluster"].sort_values())

