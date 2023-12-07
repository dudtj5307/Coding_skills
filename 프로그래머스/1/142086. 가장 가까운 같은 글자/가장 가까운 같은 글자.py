def solution(s):
    answer = []
    for i in range(len(s)-1,-1,-1):
        temp = s[i]
        for j in range(i-1, -1, -1):
            if s[j] == temp:
                answer.append(i-j)
                break
        if len(answer) == (len(s) - i -1):
            answer.append(-1)
    return answer[::-1]