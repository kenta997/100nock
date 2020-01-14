import unittest


def func(s):
    """
    入力された文字列を逆順にする

    Args:
      s (str): 文字列

    Returns:
      str: 逆順の文字列
    """

    return s[::-1]


class FuncTest(unittest.TestCase):
    def test(self):
        self.assertEqual(func("stressed"), "desserts")


unittest.main()

