def solution(n):
    b_n = bin(n)
    while True:
        n += 1
        if b_n.count('1') == bin(n).count('1'):
            return n