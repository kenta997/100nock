import pandas as pd
import re
import joblib
from tqdm import tqdm
from stemming.porter2 import stem
from func import is_in_stop_list


with open("sentiment.txt", mode="r", encoding="cp1252") as f:
    text = f.read().lower()[:-1]

y = pd.Series(
        [{"+1": 1, "-1": 0}[sentence.split()[0]]
            for sentence in tqdm(text.split("\n"), desc="make labels", leave=False)],
        name="class_label"
        ).astype("int8")
text = re.sub(r"<[^<>]+>|[\"-\/]|[:-\>]|@|[\[-`]|\+1 |\-1 ", "", text)
text = re.sub(r" [a-z] ", r" ", text)
text = re.sub(r"[0-9]+", r"0", text)
feature_words = [stem(word) for word in tqdm(text.split(), desc="stem", leave=False)]
feature_words = [word for word in tqdm(feature_words, desc="remove stop words", leave=False)
    if not is_in_stop_list(word)]
feature_words = pd.Series(feature_words).value_counts()
feature_words = feature_words[feature_words > 5].index.tolist()

with open("columns.txt", mode="w", encoding="cp1252") as f:
    f.write("\n".join(sorted(feature_words)))

X = [list(map(stem, sentence.split())) for sentence in tqdm(text.split("\n"), desc="stem", leave=False)]
X = pd.DataFrame(
        [[int(feature in sentence) for feature in feature_words]
            for sentence in tqdm(X, desc="make features", leave=False)],
    columns=list(feature_words)
    ).astype("int8")
X.sort_index(axis=1, inplace=True)
features = pd.concat([X, y], axis=1)
print(features)

joblib.dump(features, "features.joblib", compress=3)

