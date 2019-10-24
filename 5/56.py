import xml.etree.ElementTree as ET

tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

result = ["{}({})".format(coreference[1][4].text, coreference[0][4].text) for coreference in root.findall("./document/coreference/")]
print("\n".join(result))

with open("56.txt", mode="w") as f:
    f.write("\n".join(result))

