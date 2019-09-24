import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len("".join(re.findall("[a-zA-z]+", x))) for x in s.split()])

