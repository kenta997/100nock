import unittest


def func(s):
    """
    文字列から元素記号の連想配列を作成する

    Args:
      s (str): 文字列

    Returns:
      dict[int, str]: 元素記号の連想配列
    """

    return {i + 1: x[0] if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else x[:2] for i, x in enumerate(s.split())}


class FuncTest(unittest.TestCase):
    def test(self):
        s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " +\
            "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        out = {1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne",
                11: "Na", 12: "Mi", 13: "Al", 14: "Si", 15: "P", 16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca"}
        self.assertEqual(func(s), out)


unittest.main()

