from math import factorial as f

def solution(n):
    answer = 0
    for i in range(n//2 + 1):   # 2 의 개수
        print(i)
        j = n - 2 * i           # 1 의 개수
        answer += f(i+j) // (f(i) * f(j))
    return answer % 1234567