#!/usr/bin/python3
def element_at(my_list, idx):
    rang = len(my_list)
    if idx < 0:
        return("None")
    if idx > rang:
        return("None")
    return (my_list[int(idx)])
