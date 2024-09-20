import sys

N = int(input())
dp = [False, False] + [True]*(N-1)
primes = []
for i in range(2, N+1):
    if dp[i]:
        primes.append(i)
        for j in range(2*i, N+1, i):
            dp[j] = False

total, end = 0, 0
answer = 0
for start in range(len(primes)):
    while total < N and end < len(primes):
        total += primes[end]
        end += 1
    if total == N:
        answer += 1
    total -= primes[start]
print(answer)