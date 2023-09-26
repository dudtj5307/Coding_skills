def is_prime(n):
    if n == 1: return 0
    for i in range(2, int(n**(1/2))+1):
        if not n % i: return 0
    return 1

def solution(n, k):
    que = ""
    while n // k:
        que = str(n % k) + que
        n = n // k
    que = str(n) + que
    answer = 0
    s = ""
    for q in que:
        if q == "0":
            if s: answer += is_prime(int(s))
            s = ""
        else:
            s += q
    if s: answer += is_prime(int(s))
    return answer
