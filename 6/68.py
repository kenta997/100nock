import json
from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm

cli = MongoClient("localhost", 27017)
db = cli["100nock"]
col = db["artist"]

for doc in col.find(filter={"tags.value": "dance"}).sort("rating.count", -1).limit(10):
    print(doc, "\n")

