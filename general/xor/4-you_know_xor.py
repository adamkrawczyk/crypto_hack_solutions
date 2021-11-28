#!/usr/bin/python3

from pwn import *
import string

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

data xor key -> len(data == key)

data = bytes.fromhex(data)

data_crypto = b"crypto{"

flag_1 = xor(data, data_crypto)

print(flag_1)

flag_2 = xor(data, b"}")
print(flag_2)

flag = flag_1[: (len(data_crypto))]
flag += bytes(chr(flag_2[len(flag_2) - 1]), "utf-8")

flag = xor(data, flag)
print(flag)


"""
key_tab = {}

Length = len(data)
lastChar = 255
firstChar = 0

tmp = firstChar

data_to_work = [0]*Length
count = 1
while True:
    if tmp == lastChar + 1:
        seek = 1
        while seek < Length:
            if data_to_work[seek] == lastChar:
                data_to_work[seek] = firstChar
                seek = seek + 1
                count = count + 1
            else:
                data_to_work[seek]= data_to_work[seek] + 1
                seek = 1
                break

        tmp = firstChar

        if seek == Length:
            break

    data_to_work[0] = tmp
    tmp = tmp + 1
    text = [chr(a) for a in data_to_work[:count]]
    text = "".join(text)

    flag = xor(data, bytes(text, 'utf-8'))
    try:
        flag = flag.decode("utf-8")
    except:
        flag = "Error"

    if "crypto" in flag:
        print(flag)
        
    """
