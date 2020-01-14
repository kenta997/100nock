import unittest


def ngram(s, n):
    """
    シーケンスのn-gramを作成する

    Args:
      s (sequence): 文字列やリストなど
      n (int): 数値

    Returns:
      list: n-gram
    """

    return [s[i:i + n] for i in range(len(s) - n + 1)]


class Test(unittest.TestCase):
    def test(self):
        s1 = "paraparaparadise"
        s2 = "paragraph"
        X = set(ngram(s1, 2))
        Y = set(ngram(s2, 2))
        self.assertEqual(X | Y, {"pa", "ar", "ra", "ap", "ad", "di", "is", "se", "ag", "gr", "ph"})
        self.assertEqual(X & Y, {"pa", "ar", "ra", "ap"})
        self.assertEqual(X - Y, {"ad", "di", "is", "se"})
        self.assertEqual("se" in X, True)
        self.assertEqual("se" in Y, False)


unittest.main()

