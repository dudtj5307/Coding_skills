def solution(topping):
    n = len(topping)
    if n == 1: return 0

    t_dict, r_dict, t_l, r_l = {}, {}, [], []
    for i in range(0, n):
        t_dict[topping[i]] = 0
        r_dict[topping[n-1-i]] = 0
        t_l.append(len(t_dict.keys()))
        r_l.append(len(r_dict.keys()))

    answer = 0
    for i in range(0, n-1):
        if t_l[i] == r_l[n-2-i]: answer += 1
    return answer