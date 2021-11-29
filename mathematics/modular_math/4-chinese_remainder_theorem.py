#!/usr/bin/python3
import math

# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
# x ≡ a mod 935

for x in range(1, 1000000):
    if x % 5 == 2 and x % 11 == 3 and x % 17 == 5:
        print(x % 935)
        break