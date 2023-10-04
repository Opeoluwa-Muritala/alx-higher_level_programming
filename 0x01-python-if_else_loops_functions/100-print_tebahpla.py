#!/usr/bin/python3
strng = ""
i = 0
for i in range(97, 123):
    if (i % 2 == 0):
        strng= strng + chr(i-32)
    else:
        strng = strng + chr(i)
print("".join(reversed(strng)))
