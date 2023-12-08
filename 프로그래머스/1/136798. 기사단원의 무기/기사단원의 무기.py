
def solution(number, limit, power):
    weapon = [0] * (number + 1)
    for i in range(1, number+1):
        for j in range(i, number+1, i):
            weapon[j] += 1
    answer = 0
    for w in weapon:
        if w > limit:
            answer += power
        else:
            answer += w
    return answer