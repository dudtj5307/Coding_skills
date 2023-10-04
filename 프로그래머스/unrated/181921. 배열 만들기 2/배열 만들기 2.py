def solution(l, r):
    prev = [5]
    answer = [5]
    for i in range(0, len(str(r))-1):
        temp = []
        for p in prev:
            temp.extend([p*10, p*10 + 5])
        answer.extend(temp)
        prev = temp
    answer = list(filter(lambda x: l<=x<=r, answer))
    if not answer: return [-1]
    return answer
            
            