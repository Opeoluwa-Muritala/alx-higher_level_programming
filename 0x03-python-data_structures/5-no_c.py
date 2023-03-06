#!/usr/bin/python3

def no_c(my_string):
    remove = ['C','c']
    new_text = "".join(x for x in my_string if x not in list(remove))
    return new_text.strip()
