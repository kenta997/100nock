import itertools

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

result = []
for sentence in lattice:
    noun = []
    for chunk in sentence:
        if "名詞" in [x.pos for x in chunk.morphs]:
            noun.append(chunk)
    for noun_chunk1, noun_chunk2 in itertools.combinations(noun, 2):
        path1 = [""]
        is_unfound = True
        for x in noun_chunk1.morphs:
            if is_unfound and x.pos == "名詞":
                path1[0] += "X"
                is_unfound = False
            else:
                path1[0] += x.surface
        chunk_log = [noun_chunk1]
        next_chunk = noun_chunk1
        cross_flag = True
        while next_chunk.dst > -1:
            next_chunk = sentence[next_chunk.dst]
            if next_chunk is noun_chunk2:
                path1.append("Y")
                cross_flag = False
                break
            else:
                path1.append("".join([x.surface for x in next_chunk.morphs]))
                chunk_log.append(next_chunk)
        if cross_flag:
            path2 = [""]
            is_unfound = True
            for x in noun_chunk2.morphs:
                if is_unfound and x.pos == "名詞":
                    path2[0] += "Y"
                    is_unfound = False
                else:
                    path2[0] += x.surface
            next_chunk = noun_chunk2
            while not next_chunk in chunk_log:
                next_chunk = sentence[next_chunk.dst]
                path2.append("".join([x.surface for x in next_chunk.morphs]))
            path3 = path1[chunk_log.index(next_chunk):]
            path1 = path1[:chunk_log.index(next_chunk)]
            path2 = path2[:-1]
            result.append(" | ".join([" -> ".join(path1), " -> ".join(path2), " -> ".join(path3)]) + "\n")
        else:
            result.append(" -> ".join(path1) + "\n")

with open("49.txt", mode="w") as f:
    f.writelines(result)

