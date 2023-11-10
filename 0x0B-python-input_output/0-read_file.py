#!/usr/bin/python3
"""Read from a file and print"""


def read_file(filename=""):
    """Read From File"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip())
