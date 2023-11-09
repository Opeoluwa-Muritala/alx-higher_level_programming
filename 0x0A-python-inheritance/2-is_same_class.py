#!/usr/bin/python3
"""A function that returns True if the object is 
exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    if obj.__class__ is a_class:
        return True
    else:
        return False
    #return isinstance(obj, a_class)
