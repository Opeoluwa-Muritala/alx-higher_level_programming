#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastnumber = number % 10
    else:
        lastnumber += ((number * -1) % 10) * -1
    print("{:d}".format(number), end="")
