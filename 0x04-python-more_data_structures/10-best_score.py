#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    key = list(a_dictionary.keys())
    max_age = a_dictionary[key]
    for key, age in a_dictionary.items():
        if age > max_age:
            max_age = age
            key = key
    return (key)
