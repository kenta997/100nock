import CaboCha

with open("neko.txt", mode="r") as f:
    neko = f.readlines()

cabocha = CaboCha.Parser()

lattice = []
for sentence in neko:
    if sentence != "\n":
        tree = cabocha.parse(sentence)
        lattice.append(tree.toString(CaboCha.FORMAT_LATTICE))

lattice = "".join(lattice)
with open("neko.txt.cabocha", mode="w") as f:
    f.write(lattice)

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "表層形: {}\t 基本形: {}\t品詞: {}\t品詞細分類1: {}".format(self.surface, self.base, self.pos, self.pos1)

lattice = lattice.split("\nEOS")[:-1]
lattice = [x.split("\n") for x in lattice]
lattice = [[y.replace("\t", ",").split(",") for y in x] for x in lattice]
morph = [[Morph(y[0], y[7], y[1], y[2]) for y in x if len(y) >= 8] for x in lattice]

for x in morph[2]:
    print(x)

with open("40.txt", mode="w") as f:
    f.writelines(["".join([str(y) + "\n" for y in x]) for x in morph])

