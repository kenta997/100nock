import re
import unittest


def func(s):
    """
    文字列の内の各単語の文字数をカウントする

    Args:
      s (str): 文字列

    Returns:
      list[int]: 文字数のリスト
    """

    return [len("".join(re.findall("[a-zA-z]+", x))) for x in s.split()]


class FuncTest(unittest.TestCase):
    def test(self):
        s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
        out = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
        self.assertEqual(func(s), out)


unittest.main()

