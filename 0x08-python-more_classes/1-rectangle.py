#!/usr/bin/python3
""" A class to define what a rectangle is"""

class Rectangle:
    """ A class defining how a rectangle is ment to be"""
    def __init__(self, width = 0, height = 0):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Defines how height is retrieved"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Defines how width is retrieved"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets Width Attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
