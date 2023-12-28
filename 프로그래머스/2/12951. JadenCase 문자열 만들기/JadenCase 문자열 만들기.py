def solution(s):
    answer = ''
    flag = 1
    for a in s:
        if a == " ": 
            answer += a
            flag = 1
        elif a.isalpha():
            if flag == 1:
                answer += a.upper()
            else:
                answer += a.lower()
            flag = 0
        else:
            answer += a
            flag = 0
    return answer