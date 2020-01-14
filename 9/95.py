import numpy as np
import pandas as pd


for in_path in ["94_85.csv", "94_90.csv"]:
    df = pd.read_csv(in_path, usecols=["Human (mean)", "cos"]).rank(ascending=False, method="min")
    D = df["Human (mean)"] - df["cos"]
    N = len(df)
    rho = 1 - (6 * (D ** 2).sum()) / (N ** 3 - N)
    print("{}: {}".format(in_path, rho))

