with open("questions-words.txt", mode="r") as f:
    text = [x.strip().split("\n") for x in f.read().strip().split(": ")[1:]]

text = {x[0] : "\n".join(x[1:]) for x in text}

with open("91.txt", mode="w") as f:
    f.write(text["family"])

