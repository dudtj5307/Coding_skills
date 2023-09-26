def solution(want, number, discount):
    answer = 0
    dict_w = {w:0 for w in want}
    for d in discount[:sum(number)]:
        if d in want: dict_w[d] += 1
    if list(dict_w.values()) == number: answer += 1
    for i in range(0, len(discount)-sum(number)):
        if discount[i] in want: dict_w[discount[i]] -= 1
        if discount[sum(number)+i] in want: dict_w[discount[sum(number)+i]] += 1
        if list(dict_w.values()) == number: answer += 1
    return answer