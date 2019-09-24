s1 = "paraparaparadise"
s2 = "paragraph"


def ngram(s, n):
    return [s[i:i + n] for i in range(len(s) - n + 1)]


X = set(ngram(s1, 2))
Y = set(ngram(s2, 2))
print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("ss" in Y)

