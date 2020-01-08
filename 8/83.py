import pandas as pd
import csv
from tqdm import tqdm
from processing import ProcessThread


process = ProcessThread()

print("read csv ...", end="  ")
process.start()
df = pd.read_csv("82.txt", delimiter="\t", header=None, names=["t", "c"], quoting=3, keep_default_na=False)
process.done()

print("count co_occurrence ...", end="  ")
process.start()
(df["t"] + "\t" + df["c"]).value_counts().sort_index().reset_index().to_csv(
        "co_occurrence.csv", sep="\t", index=False, header=False, quoting=csv.QUOTE_ALL)
process.done()

print("count t ...", end="  ")
process.start()
df["t"].value_counts().sort_index().reset_index().to_csv(
        "count_t.csv", sep="\t", index=False, header=False, quoting=csv.QUOTE_ALL)
process.done()

print("count c ...", end="  ")
process.start()
df["c"].value_counts().sort_index().reset_index().to_csv(
        "count_c.csv", sep="\t", index=False, header=False, quoting=csv.QUOTE_ALL)
process.done()

print("N = ", len(df))

