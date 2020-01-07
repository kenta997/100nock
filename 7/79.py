import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt


df = joblib.load("features.joblib")
X = df.drop(columns="class_label")
y = df["class_label"]

model = joblib.load("model.joblib")
proba = model.predict_proba(X)[:,1]

precision, recall, theresholds = precision_recall_curve(y, proba)
plt.plot(recall, precision)
plt.title("precision-recall curve")
plt.xlabel("recall")
plt.ylabel("precision")
plt.show()

