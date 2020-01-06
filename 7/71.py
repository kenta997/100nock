import os
import pandas as pd
import re
from stemming.porter2 import stem
from func import is_in_stop_list


with open("sentiment.txt", mode="r", encoding="cp1252") as f:
    text = f.read().lower()
text = re.sub(r"<[^<>]+>|[\"-\/]|[:-\>]|@|[\[-`]|\+1 |\-1 ", "", text)
text = re.sub(r" [a-z] ", r" ", text)
text = re.sub(r"[0-9]+", r"0", text)
text = pd.Series(text.split()).apply(stem)
text = text.value_counts()
text = text.cumsum() / text.sum()
stop_list = text[text <= 0.5].index.tolist()
with open("stop_list.txt", mode="w", encoding="cp1252") as f:
    f.write("\n".join(stop_list))

words = "This is a pen .".split()
for word in words:
    print(word, "\t", is_in_stop_list(word))

