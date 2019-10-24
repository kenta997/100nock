with open("50.txt", mode="r") as f:
    nlp = f.read()

nlp = nlp.replace(" ", "\n")
print(nlp)

with open("51.txt", mode="w") as f:
    f.write(nlp)

