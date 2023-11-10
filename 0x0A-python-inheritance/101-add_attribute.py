#!/usr/bin/python3
"""Adds new attribue to an object"""


def add_attribute(className, attr, value):
    """Add attribute to an Object if possible"""
    if not hasattr(className, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(className, attr, value)
