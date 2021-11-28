#! /usr/bin/python3 
import sys

# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17

# a ≡ b mod n
# a = kn + b
# b = a-k*n

max_val = 1000

def find_lowest(a,k ,n,max_val):
    i = 0
    while(i<max_val):
        if(a == k*n+i):
            print(i)
            return(i)

        i = i + 1 


a = 11 
n = 6

a2 = 8146798528947
n2 = 17 

k = int(11 / 6)
k2 = int(8146798528947 / 17)

find_lowest(a,k,n,max_val)
find_lowest(a2,k2,n2,max_val)

# 8146798528947 ≡ y mod 17