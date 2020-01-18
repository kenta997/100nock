import random


random.seed(1)


def func(s):
    """
    各単語の文字をランダムに並び替える

    Args:
      s (str): 文字列

    Returns;
      str: 各単語の文字を並び替えた文字列
    """

    return " ".join([x[0] + "".join(random.sample(x[1:-1], len(x) - 2)) + x[-1] if len(x) > 4 else x
        for x in s.split()])


s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(func(s))

