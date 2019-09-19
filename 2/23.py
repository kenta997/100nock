with open("britain.txt", mode="r") as f:
    britain = f.readlines()

s = [x for x in britain if "==" in x]
s = [x.replace("=", "").replace("\n", "") + ", {}".format(x.count("=") // 2 - 1) for x in s]
print("\n".join(s))
