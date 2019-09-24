import re
from download import download

download("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/nlp.txt", "nlp.txt")

with open("nlp.txt", mode="r") as f:
    nlp = f.read()

nlp = re.sub("\n+", "\n", nlp)
nlp = re.split("\.|;|:|\?|!\s+[A-Z]", nlp)
for x in nlp:
    print(x)
print(nlp)

with open("50.txt", mode="w") as f:
    f.write("\n".join(nlp))

