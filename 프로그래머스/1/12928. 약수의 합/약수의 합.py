def solution(n):
    answer = set()
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)
    return sum(answer)