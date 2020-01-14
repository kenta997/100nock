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


class FuncTest(unittest.TestCase):
    def test(self):
        s = "I am an NLPer"
        self.assertEqual(ngram(s.split(), 2), [["I", "am"], ["am", "an"], ["an", "NLPer"]])
        self.assertEqual(ngram(s, 2), ["I ", " a", "am", "m ", " a", "an", "n ", " N", "NL", "LP", "Pe", "er"])


unittest.main()

