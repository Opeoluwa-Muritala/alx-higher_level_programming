#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    argv = len(sys.argv)

    for i in range(1, argv):
        print("{}: {}".format(i, sys.argv[i]))
