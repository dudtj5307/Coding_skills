
def solution(numLog):
    d = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    num = numLog[0]
    answer = ''
    for n in numLog[1:]:
        answer += d[n - num]
        num = n
    return answer