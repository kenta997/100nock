import pickle

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

result = [neko[i - 1]["表層形"] + x["表層形"] + neko[i + 1]["表層形"]
        for i, x in enumerate(neko) if x["表層形"] == "の" and neko[i - 1]["品詞"] == "名詞" and neko[i + 1]["品詞"] == "名詞"]
print("\n".join(result))

