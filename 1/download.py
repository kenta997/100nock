import requests

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

