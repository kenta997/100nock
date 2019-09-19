with open("britain.txt", mode="r") as f:
    britain = f.read()

s = britain[britain.find("|"):britain.find("\n}}")]
s = s.split("\n|")[1:]
s = [x.replace("'''''", "").replace("'''", "").replace("''", "") for x in s]

for i, x in enumerate(s):
    if "[[" in x:
        if not "File" in x or not "ファイル" in x:
            k = x.split(" = ")[0]
            v = x.split(" = ")[1]
            start = 0
            end = 0
            for j in range(v.count("[[")):
                start = v.find("[[", start)
                end = v.find("]]", start)
                mark = v[start + 2:end]
                if "|" in mark:
                    mark = mark[:mark.find("|")]
                v = v.replace(v[start:end + 2], mark)
            s[i] = k + " = " + v

temp = {x.split(" = ")[0]: x.split(" = ")[1] for x in s}
for k, v in temp.items():
    print(k + " : " + v)
