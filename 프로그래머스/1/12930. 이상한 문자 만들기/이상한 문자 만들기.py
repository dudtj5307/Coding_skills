def solution(s):
    answer = ""
    flag = 0
    for w in s:
        if w == " ":
            answer += " "
            flag = 0
        elif flag == 0:
            answer += w.upper()
            flag = 1
        else:
            answer += w.lower()
            flag = 0
    return answer