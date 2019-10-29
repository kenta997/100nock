import redis

r = redis.StrictRedis(connection_pool=redis.ConnectionPool(host="localhost", port=6379, db=0))

search = input("アーティスト名を入力 > ")

areas = set([r.get(k).decode() for k in r.keys(search + "*") if r.get(k).decode()])

if areas:
    print("{}の活動場所は{}です。".format(search, areas))
else:
    print("{}の活動場所は空値です。".format(search))


