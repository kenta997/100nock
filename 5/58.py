import xml.etree.ElementTree as ET
from tqdm import tqdm
import pandas as pd

root = ET.parse("nlp.txt.xml").getroot()

result = []

for sentence in tqdm(root.findall("./document/sentences/")):
    dependencies = [[dep.attrib["type"], dep[0].attrib["idx"], dep[1].attrib["idx"]]
            for dep in sentence.findall("./dependencies[@type='collapsed-dependencies']/")
            if dep.attrib["type"] == "nsub" or dep.attrib["type"] == "dobj"]
    dependencies = pd.DataFrame(dependencies, columns=["type", "governor", "dependent"])
    nsub = dependencies.query("type == 'nsub'")
    dobj = dependencies.query("type == 'dobj'")
    dependencies = pd.merge(nsub, dobj, on="governor")

    dot += "".join(["\tnode{} [label=\"{}\"];\n".format(token.attrib["id"], token[0].text)
        for token in sentence.findall("./tokens/token") if not token[0].text in punct])
    dot += "".join(["\tnode{} -> node{};\n".format(dep[0].attrib["idx"], dep[1].attrib["idx"])
        for dep in sentence.findall("./dependencies[@type='collapsed-dependencies']/") if not dep[1].text in punct])
    dot += "}\n"

    with open("dot/{}.dot".format(str(i).zfill(5)), mode="w") as f:
        f.write(dot)

    graph = pydotplus.graph_from_dot_file("dot/{}.dot".format(str(i).zfill(5)))
    graph.write_png("png/{}.png".format(str(i).zfill(5)))

