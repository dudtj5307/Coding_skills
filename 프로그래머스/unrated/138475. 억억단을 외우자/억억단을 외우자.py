def solution(e, starts):
    d_map = [0] * (e + 1)
    for m in range(1, int(e**(1/2))+1): d_map[m**2] += 1
    for i in range(2, e+1):
        for j in range(1, min(i, e//i+1)):
            d_map[i*j] += 2

    idx_map = [0] * (e + 1)
    max_cnt = 0
    for idx in range(e, 0, -1):
        if max_cnt <= d_map[idx]:
            max_cnt = d_map[idx]
            idx_map[idx] = idx
        else: idx_map[idx] = idx_map[idx+1]
    return [idx_map[s] for s in starts]