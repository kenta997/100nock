import json
from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm

cli = MongoClient("localhost", 27017)
db = cli["100nock"]
col = db["artist"]

search = input("アーティストの別名を入力 > ")
for doc in col.find(filter={"aliases.name": search}):
    print(doc)

