#!/usr/bin/python3
"""A Class to Raise an exception"""


class BaseGeometry():
    """Base Geometry Class"""

    def area(self):
        """An unimplemented class to calculate area"""
        raise Exception("area() is not implemented")
