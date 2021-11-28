#!/usr/bin/python3
import math

powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
# val = 0

for x in range(2, 50):
    for p in range(101, 999):
        for pw in range(100, 1000000):
            val = 0
            for i in range(0, len(powers)):
                if(pow(x,pw,p) == powers[i]):
                    val = val + 1
            if(val == len(powers) ):
                print(p,x)


x = 209 
powers = [113, 642]

for p in range(852, 999):
    val = 0
    for i in range(0, len(powers)):
        if(pow(x,pw,p) == powers[i]):
            val = val + 1
    if(val == len(powers) ):
        print(p,x)