import json
from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm

cli = MongoClient("localhost", 27017)
db = cli["100nock"]
col = db["artist"]

print(col.find(filter={"area": "Japan"}).count())

