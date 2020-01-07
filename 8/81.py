from tqdm import tqdm


with open("80.txt", mode="r") as f:
    text = f.read()

with open("countries.txt", mode="r") as f:
    countries = f.read().split("\n")

for country in tqdm(countries, leave=False):
    if len(country.split()) > 1:
        text = text.replace(country, country.replace(" ", "_"))

with open("81.txt", mode="w") as f:
    f.write(text)

