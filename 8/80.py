import re
from tqdm import tqdm


with open("enwiki-20150112-400-r100-10576.txt", mode="r") as f:
    text = f.read().split("\n")

with open("80.txt", mode="w") as f:
    for sentence in tqdm(text, leave=False):
        sentence = [re.sub(r"^[\.|,|!|\?|;|:|\(|\)|\[|\]|'|\"]|[\.|,|!|\?|;|:|\(|\)|\[|\]|'|\"]$", "", word)
                for word in sentence.split()]
        sentence = [word for word in sentence if word]
        sentence = " ".join(sentence)
        print(sentence, end="\n", file=f)

