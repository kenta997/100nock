import pickle
import collections

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

words = [x["基本形"] for x in neko]
counter = collections.Counter(words)
result = counter.most_common()

print("\n".join(list(map(str, result))))

