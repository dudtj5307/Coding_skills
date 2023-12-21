def solution(n):
    answer = set()
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            answer.update({i,n // i})
    return sum(answer)