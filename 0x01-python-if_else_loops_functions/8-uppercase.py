#!/usr/bin/python3
def to_uper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)

def uppercase(s):
    string_new = ""
    for character in s:
        string_new += "%c" % to_uper(c)
    print("{:s}".format(string_new))
