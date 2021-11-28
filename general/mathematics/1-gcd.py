#! /usr/bin/python3 

import sys

# a = 270
# b = 192
a = 66528
b = 52920

variables = [a,b]
variables.sort()
result = 0
if(a == 0 or b == 0 ):
    sys.exit("result : 0")

while(True):
    # print("var 0: ", variables[0])
    # print("var 1: ", variables[1])
    reminder = variables[1] % variables[0] 
    if(reminder == 0):
        print(variables[0])
        sys.exit("result")
    variables[1] = reminder
    variables.sort()