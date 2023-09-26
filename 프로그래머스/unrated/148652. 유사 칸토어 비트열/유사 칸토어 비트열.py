def validate(x):
    if x % 5 == 2: return 0
    if x < 5: return 1
    return validate(x//5)

def solution(n, l, r):
    answer = 0
    for i in range(l-1,r):
        answer += validate(i)
    return answer