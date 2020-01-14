import unittest


def temp(x, y, z):
    """
    テンプレートによる分生成

    Args:
      x (int): 時間
      y (str): 主語
      z (object): 補語

    Returns:
      str: テンプレート分
    """

    return "{}時の{}は{}".format(x, y, z)


class FuncTest(unittest.TestCase):
    def test(self):
        self.assertEqual(temp(12, "気温", 22.4), "12時の気温は22.4")


unittest.main()

