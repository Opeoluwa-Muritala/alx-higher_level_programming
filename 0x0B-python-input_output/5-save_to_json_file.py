#!/usr/bin/python3
"""A function that writes Object to a text file, using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Save JSON representation to a file"""

    with open(filename, 'w') as file:
        serializedObject = json.dumps(my_obj)
        file.write(serializedObject)
