import pickle
import collections
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
fp = FontProperties(fname="/mnt/c/WINDOWS/Fonts/meiryo.ttc")

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

words = [x["基本形"] for x in neko]
counter = collections.Counter(words)
result = counter.most_common(10)

plt.bar([x[0] for x in result], [x[1] for x in result])
plt.xticks(fontproperties=fp)
plt.yticks(fontproperties=fp)
plt.show()

