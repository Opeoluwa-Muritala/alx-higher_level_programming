#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number >= 0:
    lastnumber = number % 10
else:
    lastnumber = ((number * -1) % 10) * -1
string = f"Last digit of {number} is {lastnumber}"
if lastnumber > 5:
    print(f"{string} and is greater than 5")
elif lastnumber == 0:
    print(f"{string} and is 0")
elif (lastnumber < 6) and (lastnumber != 0):
    print(f"{string} and is less than 6 and not 0")
