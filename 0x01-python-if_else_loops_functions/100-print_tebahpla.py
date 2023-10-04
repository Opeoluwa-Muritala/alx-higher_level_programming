#!/usr/bin/python3
strng = ""
for i in range(97, 123):
    if (i % 2 == 1):
        strng = strng + chr(i - 32)
    else:
        strng = strng + chr(i)
print("{}".format("".join(reversed(strng))))
