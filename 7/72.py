import pandas as pd
import joblib
from tqdm import tqdm
from stemming.porter2 import stem
from func import is_in_stop_list


with open("sentiment.txt", mode="r", encoding="cp1252") as f:
    text = f.read().lower()[:-1]

feature_words = set(text.replace("+1 ", "").replace("-1 ", "").split())
feature_words = set([stem(word) for word in tqdm(feature_words, desc="unique word", leave=False)
    if not is_in_stop_list(word)])
X = [list(map(stem, sentence.split()[1:])) for sentence in tqdm(text.split("\n"), desc="stemming", leave=False)]
X = pd.DataFrame(
        [[int(feature in sentence) for feature in feature_words]
            for sentence in tqdm(X, desc="make features", leave=False)],
    columns=list(feature_words)
    )
y = pd.Series(
        [{"+1": 1, "-1": 0}[sentence.split()[0]]
            for sentence in tqdm(text.split("\n"), desc="make labels", leave=False)],
        name="label"
        )
features = pd.concat([X, y], axis=1)
print(features)

joblib.dump(features, "features.joblib", compress=3)

