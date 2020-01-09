from gensim.models import word2vec
import logging


logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)
sentences = word2vec.Text8Corpus("../8/81.txt")

model = word2vec.Word2Vec(sentences, size=300, min_count=10, window=5)
model.save("word2vec.model")

