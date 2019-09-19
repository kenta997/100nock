import pickle

with open("neko.pickle", mode="rb") as f:
    neko = pickle.load(f)

result = []
s = ""
i = 0
counter = 0
while i < len(neko):
    if neko[i]["品詞"] == "名詞":
        s += neko[i]["表層形"]
        counter += 1
    else:
        if len(s) > 0:
            if counter > 1:
                result.append(s)
            s = ""
            counter = 0
    i += 1

print("\n".join(result))

