#!/usr/bin/python3
def no_of_argc(*argv):
    c = len(argv)
    argv = str(argv)
    lis = list(argv.split())
    for i in range(0, c + 1):
        for li in lis:
            if i == 0:
                print(":")
            else:
                print(f"{i}: {li}\n")
no_of_argc(*argc)
