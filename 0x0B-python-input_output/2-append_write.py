#!/usr/bin/python3
"""Append to write to a file"""


def append_write(filename="", text=""):
    """Append to an external file with text"""
    with open(filename, 'a') as file:
        return file.write(text)
