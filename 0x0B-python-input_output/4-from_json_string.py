#!/usr/bin/python3
"""A function that returns Python Data Structure Represented By A String"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
