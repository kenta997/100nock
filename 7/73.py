import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

df = joblib.load("features.joblib")
X = df.drop(columns="class_label")
y = df["class_label"]
del df

model = LogisticRegression(random_state=0)
model.fit(X, y)
joblib.dump(model, "model.joblib", compress=3)

