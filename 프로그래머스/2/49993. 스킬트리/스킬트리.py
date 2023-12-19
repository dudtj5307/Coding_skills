def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        seq = skill[:]
        for s in sk:
            if s in seq:
                if s == seq[0]:
                    seq = seq[1:]
                else:
                    break
        else: answer += 1
    return answer