import xml.etree.ElementTree as ET
import re
from tqdm import tqdm

root = ET.parse("nlp.txt.xml").getroot()

result = []

def get_text(sentence, idx):
    return sentence.find("./tokens/token[@id='{}']/word".format(idx)).text

for parse in tqdm(root.findall("./document/sentences/sentence/parse")):
    parse = parse.text
    parse_list = list(parse)
    tag = []
    tag_flag = False
    depth = 0
    for i, c in enumerate(parse):
        if c == " ":
            if tag_flag:
                parse_list[i] = ">\n" + "\t" * depth
                tag_flag = False
            else:
                parse_list[i] = "\n" + "\t" * depth
        if tag_flag:
            if c.isalpha():
                tag[-1] += c
            else:
                tag[-1] += "x"
                parse_list[i] = "x"
        if c == "(":
            parse_list[i] = "<"
            tag_flag = True
            tag.append("")
            depth += 1
        elif c == ")":
            depth -= 1
            parse_list[i] = "\n" + "\t" * depth + "</{}>".format(tag[-1])
            tag.pop()

    parse_xml = "".join(parse_list)
    parse_xml = re.sub(r"(\t+)([^<]+)\n", r"\1<word>\2</word>\n", parse_xml)
    
    parse_root = ET.fromstring(parse_xml)
    for NP in parse_root.iter("NP"):
        result.append(" ".join([word.text for word in NP.iter("word")]))

print("\n".join(result))

with open("59.text", mode="w") as f:
    f.write("\n".join(result))

