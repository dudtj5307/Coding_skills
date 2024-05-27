from itertools import combinations
from collections import defaultdict

def find_max(dic, n):
    max_items = []
    f_dic = dict(filter(lambda x: len(x[0]) == n, dic.items()))
    s_list = sorted(f_dic.items(), key=lambda x: -x[1])
    max_num = 0
    for s in s_list:
        if s[1] < max_num: break
        max_items.append(s[0])
        max_num = s[1]
    return max_items

def solution(orders, course):
    answer = []
    d = defaultdict(int)
    for order in orders:
        for n in course:
            for c in combinations("".join(sorted(order)), n):
                d["".join(c)] += 1
    d = dict(filter(lambda x: x[1] > 1, d.items()))
    for n in course:
        answer.extend(find_max(d, n))
    return sorted(answer)