def solution(n):
    i,num = 1, 1
    while num <= n:
        num *= i
        i += 1
    return i - 2