with open("col1.txt", mode="r") as f:
    col1 = f.readlines()

with open("col2.txt", mode="r") as f:
    col2 = f.readlines()

col1_2 = [cell1.replace("\n", "") + "\t" + cell2 for cell1, cell2 in zip(col1, col2)]
with open("col1_2.txt", mode="w") as f:
    f.writelines(col1_2)

