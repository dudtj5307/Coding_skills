def solution(n):
    if n % 2: return (n + 1) * (n + 1) / 4
    else:
        return sum([i**2 for i in range(2, n+1, 2)])