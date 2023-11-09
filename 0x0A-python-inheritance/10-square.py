#!/usr/bin/python3
"""A Class That Inherits From Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Inherits Properties from rectangle and implements them"""
    def __init__(self, size):
        """set the values and initialize the class"""
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)
