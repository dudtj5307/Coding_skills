from collections import defaultdict

def solution(n):
    prime = defaultdict(int)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            prime[j] += 1
    return list(prime.values()).count(2)