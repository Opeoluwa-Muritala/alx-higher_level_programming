#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        maxi = my_list[0]
        for i in my_list:
            if maxi < i:
                maxi = i
        return maxi
    else:
        return "None"
