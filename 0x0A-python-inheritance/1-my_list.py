#!/usr/bin/python3
"""Prints a sorted list of integers"""


class MyList(list):
    """The class inherits from list"""
    def print_sorted(self):
        """returns the sorted result from values in the list"""
        print(sorted(self))
