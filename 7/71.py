import os
import pandas as pd
from func import is_in_stop_list


if not os.path.exists("stop_list.txt"):
    with open("sentiment.txt", mode="r", encoding="cp1252") as f:
        text = f.read()
    text = pd.Series(text.lower().replace("+1 ", "").replace("-1 ", "").split())
    text = text.value_counts()
    text = text.cumsum() / text.sum()
    stop_list = text[text <= 0.4].index.tolist()
    with open("stop_list.txt", mode="w", encoding="cp1252") as f:
        f.write("\n".join(stop_list))

words = pd.Series("This is a pen .".split())
for word in words:
    print(word, "\t", is_in_stop_list(word))

