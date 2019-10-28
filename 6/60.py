import json
import redis
from tqdm import tqdm

with open("artist.json", mode="r") as f:
    artist = f.read().split("\n")[:-1]
    artist_json = [json.loads(x) for x in artist]

r = redis.StrictRedis(connection_pool=redis.ConnectionPool(host="localhost", port=6379, db=0))

for i, x in enumerate(tqdm(artist_json)):
    r.set(x["name"] + str(x["id"]), x["area"] if "area" in x else "")

print("{}件登録しました。".format(i + 1))

