from download import download
import MeCab
import pickle

download("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt", "neko.txt")

with open("neko.txt", mode="r") as f:
    neko = f.read()

mt = MeCab.Tagger("-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd/")
parsed = mt.parse(neko)

with open("neko.txt.mecab", mode="w") as f:
    f.write(parsed)

parsed = parsed.split("\n")
parsed = [x.split("\t") for x in parsed]
parsed = [[x[0]] + x[1].split(",") if len(x) > 1 else x for x in parsed]
parsed = [{"表層形": x[0], "基本形": x[7], "品詞": x[1], "品詞細分類1": x[2]} for x in parsed if len(x) > 1]

with open("neko.pickle", mode="wb") as f:
    pickle.dump(parsed, f)

