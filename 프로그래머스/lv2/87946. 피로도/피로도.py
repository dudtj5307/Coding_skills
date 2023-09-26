from itertools import permutations

def solution(k, dungeons):
    cases = list(permutations(dungeons, len(dungeons)))
    answer = []
    for case in cases:
        explore = 0
        life = k
        for a, b in case:
            if life >= a:
                life -= b
                explore += 1
        answer.append(explore)
    return max(answer)