from collections import Counter

def solution(n, works):
    if sum(works) <= n: return 0
    dic = Counter(works)
    while n > 0:
        max_num = max(dic)
        val = dic.pop(max_num)
        if val <= n:
            dic[max_num-1] += val
            n -= val
        else:
            dic[max_num] += val - n
            dic[max_num-1] += n
            break
    return sum([(key ** 2) * val for key, val in dic.items()])