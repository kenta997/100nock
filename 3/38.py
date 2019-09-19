import pickle
import collections
import matplotlib.pyplot as plt

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

words = [x["基本形"] for x in neko]
counter = collections.Counter(words)
result = counter.most_common()

plt.hist([x[1] for x in result])
plt.show()

