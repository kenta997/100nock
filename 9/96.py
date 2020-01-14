import numpy as np
import pandas as pd
import csv


X = pd.read_csv("X300.csv", header=None, index_col=0, quoting=2, keep_default_na=False)

with open("countries.txt", mode="r") as f:
    countries = f.read().strip().split("\n")

X = pd.concat([X.loc[country.replace(" ", "_")]
    for country in countries if country.replace(" ", "_") in X.index], axis=1).T
X.to_csv("X300_country.csv", index=True, header=False, quoting=csv.QUOTE_NONNUMERIC)

