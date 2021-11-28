#! /usr/bin/python3 
import math

p = 26513
q = 32321

print(math.gcd(p,q))

u = 1

while True:
    v = (1 - p * u)/q
    if (v).is_integer():
        print(v)
        print(u)
        break

    u = u + 1
