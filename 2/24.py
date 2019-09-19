with open("britain.txt", mode="r") as f:
    s = f.read()

files = []
start = 0
end = 0

for i in range(s.count("File:")):
    start = s.find("File:", end) + 5
    end = s.find("|", start)
    files.append(s[start:end])

start = 0
end = 0
for i in range(s.count("ファイル:")):
    start = s.find("ファイル:", end) + 5
    end = s.find("|", start)
    files.append(s[start:end])

print("\n".join(files))
