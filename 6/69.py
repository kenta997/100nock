import json
from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm

cli = MongoClient("localhost", 27017)
db = cli["100nock"]
col = db["artist"]

tags = []
search = []
while True:
    tag = input("タグを入力(\\qで終了) > ")
    if tag == "\\q" or tag == "":
        break
    else:
        tags.append(tag)
        search.append(input("検索条件を入力 > "))

for doc in col.find(
        filter={k: int(v) if v.isdecimal() else v for k, v in zip(tags, search)}).sort("rating.count", -1):
    print(doc, "\n")

