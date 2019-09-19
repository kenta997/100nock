with open("britain.txt", mode="r") as f:
    britain = f.readlines()

s = [x for x in britain if "Category" in x or "カテゴリー" in x]
print("".join(s))
