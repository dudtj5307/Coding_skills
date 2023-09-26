from math import gcd

def dev(x, Y):
    if x == 1: return 0
    else:
        for y in Y:
            if not y % x: return 0
        return x

def solution(arrayA, arrayB):
    a, b = arrayA[0], arrayB[0]
    for i in range(1, len(arrayA)):
        a, b = gcd(a, arrayA[i]), gcd(b, arrayB[i])
    return max(dev(a,arrayB),dev(b, arrayA))