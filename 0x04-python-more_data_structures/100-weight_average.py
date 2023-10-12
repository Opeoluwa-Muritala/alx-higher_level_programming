#!/usr/bin/python3
def weight_average(my_list=[]):
    """t = tuple, w = weight, e = element"""
    if len(my_list) == 0:
        return 0
    bottom = 0
    top = 0
    for t in my_list:
        bottom += t[1]
        top += t[0] * t[1]
    average = top / bottom
    return average
