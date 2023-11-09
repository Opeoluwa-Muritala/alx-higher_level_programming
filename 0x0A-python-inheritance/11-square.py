#!/usr/bin/python3
"""A Class That Inherits From Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Inherits Properties from rectangle and implements them"""
    def __init__(self, size):
        """set the values and initialize the class"""
        self.__size = size
        self.integer_validator("size", self.__size)
        Rectangle.__init__(self, self.__size, self.__size)
    
    def __str__(self):
        """Return the string representation of the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)
