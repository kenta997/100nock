import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import distance, dendrogram, linkage, fcluster
import matplotlib.pyplot as plt


X = pd.read_csv("X300_country.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
dist = distance.pdist(X, "cosine")
link = linkage(dist, method="ward")

threshold = 0.9
plt.figure(figsize=(10, 5))
dg = dendrogram(link, labels=X.index, color_threshold=threshold, leaf_font_size=8)
plt.hlines(threshold, 0, 1000, linestyles="dashed")
plt.tight_layout()
plt.savefig("country_dendrogram.png")
plt.show()

