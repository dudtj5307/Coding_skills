from collections import Counter

def solution(n, works):
    dic = Counter(works)
    while n > 0:
        max_num = max(dic)
        if max_num == 0: break
        val = dic.pop(max_num)
        if val <= n:
            dic[max_num-1] += val
            n -= val
        else:
            dic[max_num] += val - n
            dic[max_num-1] += n
            break
    return sum([(key ** 2) * val for key, val in dic.items()])