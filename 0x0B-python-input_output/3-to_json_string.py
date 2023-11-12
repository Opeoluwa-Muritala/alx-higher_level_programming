#!/usr/bin/python3
"""A function that returns a JSON string representation"""
import json


def to_json_string(my_obj):
    """Convert to JSON string representation"""
    serializedObject = json.dumps(my_obj)

    return serializedObject
