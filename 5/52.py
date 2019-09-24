from stemming.porter2 import stem

with open("51.txt", mode="r") as f:
    nlp = f.read()

result = []
for x in nlp.split("\n"):
    if x:
        result.append(x + "\t" + stem(x) + "\n")

print("".join(result))
with open("52.txt", mode="w") as f:
    f.writelines(result)

