with open("britain.txt", mode="r") as f:
    britain = f.readlines()

s = [x for x in britain if "Category" in x or "カテゴリー" in x]
s = [x[x.find(":") + 1:] for x in s]
s = [x[:x.find("]")] for x in s]
print("\n".join(s))

