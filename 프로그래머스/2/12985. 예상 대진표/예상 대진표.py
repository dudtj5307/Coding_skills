def solution(n,a,b):
    i = 1
    a, b = min(a, b), max(a, b)
    while n // (2**(i-1)) > 1:
        if b % 2 == 0 and a + 1 == b:
            return i
        a, b = (a + int(a%2!=0))//2, (b + int(b%2!=0))//2
        i += 1