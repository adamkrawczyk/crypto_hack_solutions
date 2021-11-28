#! /usr/bin/python3 


# 11 ≡ x mod 6
# 8146798528947 ≡ y mod 17
# I guessed 3rd task result :D

# ----
# 3 * d ≡ 1 mod 13

#euler theorem
def linear_congruence(a, b, m):
    if b == 0:
        return 0

    if a < 0:
        a = -a
        b = -b

    b %= m
    while a > m:
        a -= m

    return (m * linear_congruence(m, -b, a) + b) // a

print(linear_congruence(3, 1, 13))