d = {'w': 1, 's': -1, 'd': 10, 'a': -10}
def solution(n, control):
    return n + sum([d[i] for i in control])