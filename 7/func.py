def is_in_stop_list(word, stop_list=""):
    """
    単語がストップリストに含まれているかどうかを判定する関数
    :word: 判定する単語
    :stop_list: ストップリストのパス(空文字の場合は./stop_list.txt)
    :return: 単語がストップリストに含まれている場合は真、それ以外は偽
    """
    with open(stop_list if stop_list else "stop_list.txt", mode="r", encoding="cp1252") as f:
        stop_list = f.read().split()
    return word.lower() in stop_list

