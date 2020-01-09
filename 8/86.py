import pandas as pd


X = pd.read_csv("X300.csv", header=None, index_col=0, quoting=2, keep_default_na=False)
print(X.loc["United_States"].values)

