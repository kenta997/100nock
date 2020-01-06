import joblib
from sklearn.linear_model import LogisticRegression


df = joblib.load("features.joblib")
X = df.drop(columns="class_label")
y = df["class_label"]

model = joblib.load("model.joblib")
pred = model.predict(X)
proba = model.predict_proba(X)

result = "\n".join([
    "\t".join([str(sentence[0]), str(sentence[1]), str(sentence[2])]) for sentence in zip(y, pred, proba)
    ])

with open("labeling.txt", mode="w", encoding="cp1252") as f:
    f.writelines(result)

print("".join(result))

