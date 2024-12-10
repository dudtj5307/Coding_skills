from collections import defaultdict

def solution(enroll, referral, seller, amount):
    dict_ref = {e:r for e, r in zip(enroll, referral)}   # 추천인 dict
    dict_answer = defaultdict(int)
    for name, cnt in zip(seller, amount):
        cost = 100 * cnt
        while name != "-":
            cost_ref = cost // 10
            dict_answer[name] += cost - cost_ref
            cost = cost_ref
            name = dict_ref[name]
            if cost < 1: break
        
    return [dict_answer[e] for e in enroll]