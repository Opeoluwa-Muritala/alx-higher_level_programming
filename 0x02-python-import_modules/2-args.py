#!/usr/bin/python3
import sys

argv = len(sys.argv)

for i in range(1, argv):
    print("{}: {}".format(i, sys.argv[i]))
