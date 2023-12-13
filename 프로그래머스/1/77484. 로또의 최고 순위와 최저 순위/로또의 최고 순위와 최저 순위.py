def solution(lottos, win_nums):
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    a = len(set(lottos) & set(win_nums))
    _max, _min = a, a
    for i in range(len(lottos)):
        if lottos[i] == 0:
            _max += 1
    return [min(6, 7-_max), min(6, 7-_min)]