import random
from tqdm import tqdm

random.seed(1)

with open("81.txt", mode="r") as text, open("82.txt", mode="w") as out:
    for sentence in tqdm(text, leave=False):
        sentence = sentence.strip().split()
        for i, t in enumerate(sentence):
            d = random.randint(1, 5)
            for j in range(max([0, i - d]), min([i + d + 1, len(sentence)])):
                if i != j:
                    out.write("{}\t{}\n".format(t, sentence[j]))

