#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from base geometry"""

    def __init__(self, width, height):
        """Creates the private variables height, width and validate them"""
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)

    def area(self):
        self.area = self.__width * self.__height
        return self.area
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

