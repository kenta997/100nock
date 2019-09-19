with open("britain.txt", mode="r") as f:
    britain = f.read()

s = britain[britain.find("|"):britain.find("\n}}")]
s = s.split("\n|")[1:]
s = [x.replace("'''''", "").replace("'''", "").replace("''", "") for x in s]

for i, x in enumerate(s):
    k = x.split(" = ")[0]
    v = x.split(" = ")[1]
    if "[[" in v:
        start = 0
        end = 0

        for j in range(v.count("[[")):
            start = v.find("[[", end)
            end = v.find("]]", start) + 2
            mark = v[start + 2:end - 2]
            if "|" in mark:
                mark = mark[:mark.find("|")]
            len_v = len(v)
            v = v.replace(v[start:end], mark)
            end -= len_v - len(v)

    if "<ref " in v or "</ref>" in v:
        v = v[:v.find("<ref")]

    if "<br />" in v:
        v = v.replace("<br />", " ")

    if "<br/>" in v:
        v = v.replace("<br/>", "\n")

    if "{{" in v:
        start = 0
        end = 0
        for j in range(v.count("{{")):
            start = v.find("{{", end)
            end = v.find("}}", start) + 2
            mark = v[start + 2:end - 2]
            if "|" in mark:
                mark = mark[mark.rfind("|") + 1:]
                len_v = len(v)
                v = v.replace(v[start:end], mark)
                end -= len_v - len(v)
    s[i] = k + " = " + v

temp = {x.split(" = ")[0]: x.split(" = ")[1] for x in s}
for k, v in temp.items():
    print(k + " : " + v)
