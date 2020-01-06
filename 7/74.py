import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression


df = joblib.load("features.joblib")
X = df.drop(columns="class_label")
y = df["class_label"]

model = joblib.load("model.joblib")
proba = model.predict_proba(X)

for label, p in zip(y, proba):
    print({0: "-1", 1:"+1"}[label], p)

