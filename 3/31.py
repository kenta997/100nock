import pickle

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

result = [x["表層形"] for x in neko if x["品詞"] == "動詞"]
print("\n".join(result))

