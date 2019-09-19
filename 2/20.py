import json
from subprocess import call
from download import download

download("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz", "jawiki-country.json.gz", True)
call(["gunzip", "jawiki-country.json.gz"])

with open("jawiki-country.json", mode="r") as f:
    s = [json.loads(x) for x in f.readlines()]

for j in s:
    if j["title"] == "イギリス":
        break

s = j["text"]
print(s)

with open("britain.txt", mode="w") as f:
    f.write(s)

