#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    rang = len(my_list)
    if idx < 0:
        return("None")
    if idx > rang:
        return(my_list)
    my_list[idx] = element
    return(my_list)
