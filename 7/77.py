import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score


with open("labeling.txt", mode="r", encoding="cp1252") as f:
    result = f.read().split("\n")

result = [x.split("\t") for x in result]
result = pd.DataFrame(result, columns=["label", "pred", "proba"]).astype({"label": "int8", "pred": "int8"})

print("prescision:\t", precision_score(result["label"], result["pred"]))
print("recall:\t\t", recall_score(result["label"], result["pred"]))
print("f1:\t\t", f1_score(result["label"], result["pred"]))

