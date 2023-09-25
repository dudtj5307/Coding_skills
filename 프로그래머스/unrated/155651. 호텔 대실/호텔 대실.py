from collections import deque
import copy

def solution(book_time):
    
    b_list = []
    for bs, be in book_time:
        b_list.append([int(bs[0:2]) * 60 + int(bs[3:5]),int(be[0:2]) * 60 + int(be[3:5])])
    b_list = sorted(b_list)
    
    que = []
    max_q = 1
    for ts, te in b_list:
        for i, q in enumerate(que):
            if q[1] + 10 <= ts: del que[i]; i-=1
        que.append([ts,te])
        max_q = max(max_q, len(que))
    return max_q