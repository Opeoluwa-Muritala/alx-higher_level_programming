#!/usr/bin/python3
from calculator_1 import add,sub,div,mul
import sys

num_arguments = len(sys.argv) - 1
arguments = sys.argv[1:]
if (num_arguments == 3):
    a = int(arguments[0])
    b = int(arguments[2])
    operator = arguments[1]
    if (operator == "+"):
        print("{} + {} = {}".format(a,b,add(a, b)))
    elif (operator == "-"):
        print("{} - {} = {}".format(a,b,sub(a, b)))
    elif (operator == "*"):
        print("{} * {} = {}".format(a,b,mul(a, b)))
    elif (operator == "/"):
        print("{} / {} = {}".format(a,b,div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
else:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
