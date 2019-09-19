from random import sample

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(" ".join([x[0] + "".join(sample(x[1:-1], len(x) - 2)) + x[-1] if len(x) > 4 else x for x in s.split()]))

