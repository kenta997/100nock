import xml.etree.ElementTree as ET

tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

result = [word.text for word, ner in zip(root.iter("word"), root.iter("NER")) if ner.text == "PERSON"]
print("\n".join(result))

with open("55.txt", mode="w") as f:
    f.write("\n".join(result))

