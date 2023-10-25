#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if type(i) != int:
                continue
            else:
                print("{:d}".format(i), end="")
                count += 1
        print()
        return count
    except (ValueError, TypeError):
        print()
        return count
