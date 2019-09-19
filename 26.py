with open("britain.txt", mode="r") as f:
    britain = f.read()

s = britain[britain.find("|"):britain.find("\n}}")]
s = s.split("\n|")[1:]
temp = {x.split(" = ")[0]: x.split(" = ")[1].replace("'''''", "").replace("'''", "").replace("''", "") for x in s}
for k, v in temp.items():
    print(k + " : " + v)
