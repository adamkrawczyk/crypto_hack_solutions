#!/usr/bin/python3

p = 29
ints = [14, 6, 11]

for x in ints:
    for a in range(p-1):
        b = (a*a)%p
        if b == x:
            print("x is a quadratic residue : ", x)
            print("for a value : ",a)
        else:
            continue