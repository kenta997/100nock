import json
import redis
from tqdm import tqdm

r = redis.StrictRedis(connection_pool=redis.ConnectionPool(host="localhost", port=6379, db=1))

if len(r.keys()) == 0:
    with open("artist.json", mode="r") as f:
        artist = f.read().split("\n")[:-1]
        artist_json = [json.loads(x) for x in artist]

    for i, x in enumerate(tqdm(artist_json)):
        r.set(x["name"] + " " + str(x["id"]), json.dumps(x["tags"]) if "tags" in x else "")

    print("{}件登録しました。".format(i + 1))

search = input("アーティスト名を入力 > ")
keys = r.keys(search + "*")
for k in keys:
    print("{}のタグ".format(k.decode()))
    tags = r.get(k).decode()
    if tags:
        tags = json.loads(r.get(k).decode())
        for tag in tags:
            print("\ttag: {}, count: {}".format(tag["value"], tag["count"]))
    else:
        print("\tタグ情報はありません。")

