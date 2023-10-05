def solution(spell, dic):
    s = set(spell)
    for d in dic:
        if s == set(d):
            return 1
    return 2