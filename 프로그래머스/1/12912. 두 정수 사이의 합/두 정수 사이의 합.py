def solution(a, b):
    return sum(range(a,b+1)) if a ==b else sum(range(a,b+1)) + sum(range(b,a+1))