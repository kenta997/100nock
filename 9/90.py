import pandas as pd
import csv
from gensim.models import word2vec
import logging


logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)
sentences = word2vec.Text8Corpus("../8/81.txt")

model = word2vec.Word2Vec(sentences, size=300, min_count=5, window=5)
model.save("word2vec.model")

X = pd.DataFrame(model.wv.vectors, index=model.wv.index2word).sort_index()
X.to_csv("X300.csv", index=True, header=False, quoting=csv.QUOTE_NONNUMERIC)
