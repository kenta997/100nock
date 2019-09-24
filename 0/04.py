s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. " \
    "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
print({i + 1: x[0] if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else x[:2] for i, x in enumerate(s.split())})

