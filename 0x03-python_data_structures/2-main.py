#!/usr/bin/python3
replace = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 30
new_element = 9
new_list = replace(my_list, idx, new_element)
print(my_list)
print(new_list)
