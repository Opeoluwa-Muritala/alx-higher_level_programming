#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

# Get the last digit
if number > 0:
    last_digit = number % 10
else:
    last_digit = number % -10

# Perform checks on the last digit
if int(last_digit) > 5:
    end = "and is greater than 5"
elif int(last_digit) == 0:
    end = "and is 0"
elif (int(last_digit) < 6) & (int(last_digit) != 0):
    end = "and is less than 6 and not 0"


# Provide needed output
print(f"Last digit of {number} is {last_digit}", end=" ")
print(end)
