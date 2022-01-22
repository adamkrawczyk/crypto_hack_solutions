#!/usr/bin/python3
# import math

# math.inverse(209, 991)
g = 209
p = 991

for i in range(1,5000):
    if(g* i % p ==1):
        print(i)
        
