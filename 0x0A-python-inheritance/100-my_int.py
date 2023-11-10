#!/usr/bin/python3
"""A Class That Inherits From Int"""


class MyInt(int):
    """A rebel class"""

    def __eq__(self, value):
        """Invert Equality"""
        return int.__ne__(self, value)

    def __ne__(self, value):
        """Invert Inequality"""
        return int.__eq__(self, value)
