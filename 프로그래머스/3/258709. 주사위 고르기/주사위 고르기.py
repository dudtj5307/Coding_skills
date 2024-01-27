from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    N = len(dice)
    answer = {}
    for A_idx in combinations(range(N), N//2):
        B_idx = tuple([i for i in range(0, N) if i not in A_idx])
        A_sum, B_sum = [], []
        for dice_num in product(range(6), repeat=N//2):
            A_sum.append(sum(dice[i][j] for i, j in zip(A_idx, dice_num)))
            B_sum.append(sum(dice[i][j] for i, j in zip(B_idx, dice_num)))
        B_sum.sort()
        _sum = sum([bisect_left(B_sum, a) for a in A_sum])
        answer[_sum] = A_idx
    return list(map(lambda x:x+1, answer[max(answer.keys())]))

        