#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Returns an object from JSON file"""
    with open(filename, 'r') as JSON_file:
        fileContents = JSON_file.read()
        return json.loads(fileContents)
