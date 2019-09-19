import pickle

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

result = [x["表層形"] for x in neko if x["品詞"] == "名詞" and x["品詞細分類1"] == "サ変接続"]
print("\n".join(result))

