import unittest


def cipher(s):
    """
    文字列を暗号化する
    
    Args:
      s (str): 文字列

    Returns:
      str: 暗号化された文字列
    """

    return "".join([str(219 - ord(x)) if "a" <= x <= "z" else x for x in s])


def uncipher(s):
    """
    暗号化された文字列を復号化する

    Args:
      s (str): 暗号化された文字列

    Returns:
      str: 元の文字列
    """

    result = ""
    i = 0
    while i < len(s):
        if s[i].isdecimal():
            result += chr(219 - int(s[i:i + 3]))
            i += 3
        else:
            result += s[i]
            i += 1
    return result


class FuncTest(unittest.TestCase):
    def test(self):
        s = "I'm a perfect human."
        self.assertEqual(cipher(s), "I'110 122 107118105117118120103 115102110122109.")
        self.assertEqual(uncipher(cipher(s)), s)


unittest.main()

