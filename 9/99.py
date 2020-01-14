import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


X = pd.read_csv("X300_country.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
X_tsne = TSNE(metric="euclidean", random_state=1).fit_transform(X)

for x, y, label in zip(X_tsne[:, 0], X_tsne[:, 1], X.index):
    plt.text(x, y, label)
plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
plt.show()

