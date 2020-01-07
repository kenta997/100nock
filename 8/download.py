import requests
from subprocess import call

def download(url, name="downloaded.txt", is_bin=False):
    try:
        r = requests.get(url)
        if is_bin:
            with open(name, mode="wb") as f:
                f.write(r.content)
        else:
            r.encoding = r.apparent_encoding
            with open(name, mode="w") as f:
                f.write(r.text)
    except requests.exceptions.RequestException as err:
        print(err)

if __name__ == "__main__":
    download("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/enwiki-20150112-400-r100-10576.txt.bz2",
            "enwiki-20150112-400-r100-10576.txt.bz2",
            True)
    call(["bunzip2", "enwiki-20150112-400-r100-10576.txt.bz2"])

