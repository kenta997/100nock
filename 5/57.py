import xml.etree.ElementTree as ET
import pydotplus
from tqdm import tqdm

root = ET.parse("nlp.txt.xml").getroot()
punct = set([x.text for x in root.findall(
    "./document/sentences/sentence/dependencies[@type='collapsed-dependencies']/dep[@type='punct']/dependent")])

for i, sentence in enumerate(tqdm(root.findall("./document/sentences/"))):
    dot = "digraph graph{}".format(i) + " {\n"
    dot += "\tnode0 [label=\"ROOT\"];\n"
    dot += "".join(["\tnode{} [label=\"{}\"];\n".format(token.attrib["id"], token[0].text)
        for token in sentence.findall("./tokens/token") if not token[0].text in punct])
    dot += "".join(["\tnode{} -> node{};\n".format(dep[0].attrib["idx"], dep[1].attrib["idx"])
        for dep in sentence.findall("./dependencies[@type='collapsed-dependencies']/") if not dep[1].text in punct])
    dot += "}\n"

    with open("dot/{}.dot".format(str(i).zfill(5)), mode="w") as f:
        f.write(dot)

    graph = pydotplus.graph_from_dot_file("dot/{}.dot".format(str(i).zfill(5)))
    graph.write_png("png/{}.png".format(str(i).zfill(5)))

