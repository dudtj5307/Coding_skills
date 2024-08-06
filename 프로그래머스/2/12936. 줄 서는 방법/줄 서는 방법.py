from math import factorial as fac

def solution(n, k):
    num_list = [i for i in range(1, n+1)]
    answer = []
    r = k - 1
    while n > 1:
        n -= 1
        if n == 1: 
            answer.append(num_list.pop(r))
            break
        q, r = divmod(r, fac(n))
        answer.append(num_list.pop(q))
    return answer + num_list