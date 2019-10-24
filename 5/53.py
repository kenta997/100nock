from stemming.porter2 import stem
from download import download
from subprocess import call
import xml.etree.ElementTree as ET

# download("http://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip", "stanford-corenlp-full-2018-10-05.zip", True)
# call(["unzip", "stanford-corenlp-full-2018-10-05.zip"])

stanford = "stanford-corenlp-full-2018-10-05/"

call(["bash", stanford + "corenlp.sh", "-file", "nlp.txt"])

tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

result = [name.text for name in root.iter("word")]
print("\n".join(result))

with open("53.txt", mode="w") as f:
    f.write("\n".join(result))

