#!/usr/bin/python3
import random.randint
number = random.randint(-10000,10000)
string = "Last digit of {} is {1:}".format(number,number)
lastnumber = int("{1:}".format(number))
if lastnumber > 5:
    print(f"{string} and is greater than 5")
elif lastnumber == 0:
     print(f"{string} and is 0")
elif (lastnumber < 6) and (lastnumber != 0):
     print(f"{string} and is less than 6 and not 0")
