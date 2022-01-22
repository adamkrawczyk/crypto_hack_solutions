#!/usr/bin/python3
from gmpy2 import iroot
from functools import reduce
from itertools import combinations
from Crypto.Util.number import inverse , long_to_bytes

exec(open("/home/adam/projects/github/crypto_hack/RSA/PUBLIC_EXPONENT/output.txt" , "r").read())

def CRT(r, mod):
    M = reduce(lambda x,y:x*y, mod)

    ans = 0
    
    for i in range(len(r)):
        m = M // mod[i]
        ans += r[i] * m * inverse(m, mod[i])
    
    return ans % M

ls = list(combinations(range(1 , 8) , 3))
e = 3 

for l in ls:
    exec("n = [n{} , n{} , n{}]".format(l[0] , l[1] , l[2]))
    exec("c = [c{} , c{} , c{}]".format(l[0] , l[1] , l[2]))

    m = CRT(c , n)
    flag = long_to_bytes(iroot(m , e)[0]).decode("latin-1")

    if "crypto" in flag:
        print(l)
        print(flag)
        break
