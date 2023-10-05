#!/usr/bin/python3
import sys

argv = sys.argv[1:]
add = 0

for index, arg in enumerate(argv):
    add += int(arg)

print(add)
