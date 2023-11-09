#!/usr/bin/python3
"""Baseclass Geometery Continuation"""

class BaseGeometry():
    """Class to perform non implemented basic operations"""
    def area(self):
        """Unimplemented Class To Check area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Check if the value is an integer """
        if type(value) !=  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
