#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number_arguments = len(sys.argv) - 1
    argv = sys.argv[1:]

    if (len(argv) != 0):
        strng = "arguments" if len(argv) > 1 else "argument"
        print("{} {}:".format(number_arguments, strng))
        for index, arg in enumerate(argv, start=1):
            print("{}: {}".format(index, arg))
    else:
        print("0 arguments.")
