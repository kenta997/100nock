import xml.etree.ElementTree as ET

tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

result = ["\t".join(list(map(lambda x: x.text, name))) for name in zip(root.iter("word"), root.iter("lemma"), root.iter("POS"))]
print("\n".join(result))

with open("54.txt", mode="w") as f:
    f.write("\n".join(result))

