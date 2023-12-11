def solution(clothes):
    dic = {}
    for _, category in clothes:
        if category not in dic.keys():
            dic[category] = 2
        else: dic[category] += 1
    answer = 1
    for value in dic.values():
        answer *= value
    return answer - 1


