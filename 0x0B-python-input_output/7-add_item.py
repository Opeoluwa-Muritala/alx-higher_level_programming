#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them to a file"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file= __import__('6-load_from_json_file').load_from_json_file


def add_item(item, filename = "add_item.json"):
    """Create A list in a JSON file and Append New Items to It"""
    try:
        jsonItems = load_from_json_file(filename)
    except FileNotFoundError:
        jsonItems = []
    jsonItems.extend(sys.argv[1:])
    save_to_json_file(jsonItems, filename)
