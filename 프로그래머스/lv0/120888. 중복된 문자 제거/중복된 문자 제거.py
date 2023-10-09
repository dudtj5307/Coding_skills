def solution(my_string):
    temp = ""
    answer = ""
    for s in my_string:
        if s not in temp:
            answer += s
            temp += s
    return answer