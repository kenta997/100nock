def cipher(s):
    return "".join([str(219 - ord(x)) if x >= "a" and x <= "z" else x for x in s])

s = cipher("I'm a perfect human.")
print(s)
uncipher = ""
i = 0
while i < len(s):
    if s[i].isdecimal():
        uncipher += chr(219 - int(s[i:i + 3]))
        i += 3
    else:
        uncipher += s[i]
        i += 1
print(uncipher)
