import unittest


def func(s1, s2):
    """
    二つの文字列を交互に連結する

    Args:
      s1 (str): 一つ目の文字列
      s2 (str): 二つ目の文字列

    Returns:
      str: 文字列
    """
    
    return "".join([x + y for x, y in zip(s1, s2)])


class FuncTest(unittest.TestCase):
    def test(self):
        self.assertEqual(func("パトカー", "タクシー"), "パタトクカシーー")


unittest.main()

