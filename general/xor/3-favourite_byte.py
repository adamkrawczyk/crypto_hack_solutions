#!/usr/bin/python3
from pwn import *
import string

KEY = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

KEY = bytes.fromhex(KEY)

for i in range(128): # ascii size
    flag = xor(KEY, i)
    try:
        flag = flag.decode("utf-8")
    except:
        flag = "Error"

    if "crypto" in flag:
        print(flag)
