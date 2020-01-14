import unittest


def func(s):
    """
    文字列の偶数番目の文字のみを抽出

    Args:
      s (str): 文字列

    Returns:
      str: 偶数番目の文字で構成された文字列
    """

    return s[::2]


class FuncTest(unittest.TestCase):
    def test(self):
        self.assertEqual(func("パタトクカシーー"), "パトカー")


unittest.main()

