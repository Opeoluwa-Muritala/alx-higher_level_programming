#!/usr/bin/python3
def remove_char_at(str, n):
    if -1 < n < len(str):
        str = str.replace(str[n], '')
    else:
        str = str
    return str
