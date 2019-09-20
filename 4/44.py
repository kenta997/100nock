import CaboCha
import os
import pydotplus
from tqdm import tqdm

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "表層形: {}\t 基本形: {}\t品詞: {}\t品詞細分類1: {}".format(
                self.surface, self.base, self.pos, self.pos1)

class Chunk:
    def __init__(self, morphs, dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

    def add_src(self, src):
        self.srcs.append(src)

    def __str__(self):
        return "形態素:\n{}\n係り先文節インデックス番号: {}\n係り元文節インデックス番号: {}".format(
                "\n".join(["\t" + str(x) for x in self.morphs]), self.dst, self.srcs)


with open("neko.txt.cabocha", mode="r") as f:
    lattice = f.read()

lattice = lattice.split("\nEOS")[:-1]
lattice = [x.split("* ")[1:] for x in lattice]
lattice = [[y.split("\n") for y in x] for x in lattice]
lattice = [[[y[0].split(" ")] + [z.replace("\t", ",").split(",") for z in y[1:]] for y in x] for x in lattice]
lattice = [[Chunk([Morph(z[0], z[7], z[1], z[2]) for z in y[1:] if len(z) >= 8], int(y[0][1][:-1])) for y in x] for x in lattice]

for x in lattice:
    for i, y in enumerate(x):
        dst = y.dst
        if dst != -1:
            x[dst].add_src(i)


for i, sentence in enumerate(tqdm(lattice)):
    dot = "digraph graph{}".format(i) + " {\n"
    dot += "".join(["\tnode{} [label=\"{}\"];\n".format(j, "".join([morph.surface for morph in chunk.morphs]))
        for j, chunk in enumerate(sentence)])
    dot += "".join(["\tnode{} -> node{};\n".format(j, chunk.dst)
        for j, chunk in enumerate(sentence) if chunk.dst != -1])
    # for j, chunk in enumerate(sentence):
        # if chunk.dst != -1:
            # dot += "\tnode{} [label=\"".format(j)
            # dot += "".join([morph.surface for morph in chunk.morphs])
            # dot += "\"] -> node{} [label=\"".format(chunk.dst)
            # dot += "".join([morph.surface for morph in sentence[chunk.dst].morphs])
            # dot += "\"];\n"
            # dot[-1].append("\t" + "".join([morph.surface for morph in chunk.morphs]) + " -> "\
            #         + "".join([morph.surface for morph in sentence[chunk.dst].morphs]) + ";\n")
    dot += "}\n"
    with open("dot/{}.dot".format(i), mode="w") as f:
        f.write(dot)

    graph = pydotplus.graph_from_dot_file("dot/{}.dot".format(i))
    graph.write_png("png/{}.png".format(i))

