#!/usr/bin/python3
"""First Base Class"""


class Base():
    """Main Base Class"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Intitialize Base Class"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
