import redis
from tqdm import tqdm

r = redis.StrictRedis(connection_pool=redis.ConnectionPool(host="localhost", port=6379, db=0))

num = len([k.decode() for k in tqdm(r.keys()) if r.get(k).decode() == "Japan"])
print(num)

