#!/usr/bin/python3
 
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return bytes(sum(matrix, []))

def add_round_key(s, k):
    tmp = k
    for i in range(0, 4):
        for e in range(0, 4):
            tmp[i][e] = k[i][e] ^ s[i][e]

    return matrix2bytes(list(tmp))
    # return v


print(add_round_key(state, round_key))

