import xml.etree.ElementTree as ET
from tqdm import tqdm
import pandas as pd

root = ET.parse("nlp.txt.xml").getroot()

result = []

def get_text(sentence, idx):
    return sentence[0][idx - 1][0].text

for sentence in tqdm(root.findall("./document/sentences/")):
    dependencies = [[dep.attrib["type"], dep[0].attrib["idx"], dep[1].attrib["idx"]]
            for dep in sentence.findall("./dependencies[@type='collapsed-dependencies']/")
            if dep.attrib["type"] == "nsubj" or dep.attrib["type"] == "dobj"]
    dependencies = pd.DataFrame(dependencies, columns=["type", "governor", "dependent"])
    nsub = dependencies.query("type == 'nsubj'")[["governor", "dependent"]]
    dobj = dependencies.query("type == 'dobj'")[["governor", "dependent"]]
    dependencies = pd.merge(nsub, dobj, on="governor", how="outer", suffixes=["_subj", "_obj"])
    dependencies["subject"] = dependencies["dependent_subj"].apply(
            lambda x: get_text(sentence, int(x)) if not pd.isna(x) else "")
    dependencies["predicate"] = dependencies["governor"].apply(lambda x: get_text(sentence, int(x)))
    dependencies["object"] = dependencies["dependent_obj"].apply(
            lambda x: get_text(sentence, int(x)) if not pd.isna(x) else "")
    dependencies["result"] = dependencies["subject"] + "\t" + dependencies["predicate"] + "\t" + dependencies["object"]
    for x in dependencies["result"].values:
        result.append(x)

print("\n".join(result))

with open("58.text", mode="w") as f:
    f.write("\n".join(result))

