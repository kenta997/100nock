import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate


df = joblib.load("features.joblib")
X = df.drop(columns="class_label")
y = df["class_label"]
model = LogisticRegression(random_state=1, solver="lbfgs")
result = cross_validate(model, X, y, scoring=["precision", "recall", "f1"], cv=5)

print("precision:")
print(result["test_precision"])
print()

print("recall:")
print(result["test_recall"])
print()

print("f1:")
print(result["test_f1"])


