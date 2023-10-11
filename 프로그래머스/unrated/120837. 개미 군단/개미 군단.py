def solution(hp):
    answer = 0
    for d in [5, 3, 1]:
        answer += hp // d
        hp = hp % d
    return answer