#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    add = 0

    for index, arg in enumerate(argv):
        add += int(arg)

    print(add)
