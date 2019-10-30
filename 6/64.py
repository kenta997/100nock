import json
from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm

with open("artist.json", mode="r") as f:
    artist = f.read().split("\n")[:-1]
    artist_json = [json.loads(x) for x in artist]

cli = MongoClient("localhost", 27017)
db = cli["100nock"]
col = db["artist"]

if col.count() == 0:
    result = col.insert_many(artist_json)

col.create_index("name")
col.create_index("aliases.name")
col.create_index("tags.value")
col.create_index("rating.value")

