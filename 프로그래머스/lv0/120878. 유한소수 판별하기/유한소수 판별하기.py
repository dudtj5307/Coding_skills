def solution(a, b):
    for i in range(2, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            a //= i
            b //= i
    if b == 1: return 1
    while b % 2 == 0 or b % 5 == 0:
        if b % 2 == 0: b //= 2
        if b % 5 == 0: b //= 5
        if b == 1: return 1
    return 2