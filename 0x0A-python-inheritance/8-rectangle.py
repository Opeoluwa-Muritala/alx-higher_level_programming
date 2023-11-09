#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Inherits from base geometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)
