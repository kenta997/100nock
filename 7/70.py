import codecs
import random

encoding = "cp1252"
with codecs.open("rt-polaritydata/rt-polarity.pos", mode="r", encoding=encoding) as f:
    pos = f.readlines()

with codecs.open("rt-polaritydata/rt-polarity.neg", mode="r", encoding=encoding) as f:
    neg = f.readlines()

pos = ["+1 " + x for x in pos]
neg = ["-1 " + x for x in neg]
cat = pos + neg

random.seed(777)
random.shuffle(cat)

with open("sentiment.txt", mode="w", encoding=encoding) as f:
    f.writelines(cat)

pos_num = 0
neg_num = 0
for x in cat:
    if x.startswith("+1"):
        pos_num += 1
    elif x.startswith("-1"):
        neg_num += 1

print("pos: {}, neg: {}".format(pos_num, neg_num))

