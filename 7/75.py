import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression


columns = joblib.load("features.joblib").drop(columns="class_label").columns
model = joblib.load("model.joblib")
coef = pd.Series(model.coef_[0], index=columns).abs().sort_values()
print(coef.tail(10)[::-1])
print(coef.head(10))


