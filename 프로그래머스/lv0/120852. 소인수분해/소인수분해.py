def prime(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

def solution(n):
    answer = set()
    while True:
        i = prime(n)
        n //= i
        answer.add(i)
        if n == 1:
            return sorted(list(answer))