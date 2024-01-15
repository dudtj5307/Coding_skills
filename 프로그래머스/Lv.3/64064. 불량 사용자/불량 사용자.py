from itertools import permutations
from collections import defaultdict

def masked(string, i_list):
    l_s = list(string)
    for i in i_list:
        l_s[i] = "*"
    return "".join(l_s)
        
def solution(user_id, banned_id):
    mask = defaultdict(list)
    for i, ban in enumerate(banned_id):
        for j in range(len(ban)):
            if ban[j] == "*":
                mask[i].append(j)
    answer = []
    for ids in permutations(user_id, len(banned_id)):
        # print(ids)
        for i in range(len(ids)):
            if len(ids[i]) != len(banned_id[i]):
                break
            else:
                if masked(ids[i], mask[i]) != banned_id[i]:
                    break
        else:
            if set(ids) not in answer:
                answer.append(set(ids))
    return len(answer)
                