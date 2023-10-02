#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
        language that combines remarkable power with very clear syntax"
str = str[39:(92-26)] + " " + str[114:118] + " " + str[:6]
print(str)
