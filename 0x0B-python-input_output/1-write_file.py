#!/usr/bin/python3
"""Write into an external File"""


def write_file(filename="", text=""):
    """Write A File"""
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)
