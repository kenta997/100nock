import numpy as np
from sklearn.metrics import accuracy_score


for file_num in [85, 90]:
    with open("92_{}.txt".format(file_num), mode="r") as f:
        text = [x.strip().split(" ")[3:5] for x in f.read().strip().split("\n")]
    print("accuracy {}: {}".format(file_num, accuracy_score([x[0] for x in text], [x[1] for x in text])))

