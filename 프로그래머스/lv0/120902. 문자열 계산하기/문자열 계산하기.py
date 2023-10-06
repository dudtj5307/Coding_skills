def solution(my_string):
    answer = 0
    l_string = my_string.split(" ")
    flag = 1
    for s in l_string:
        if flag == 0:
            if s == "+": flag = 1
            elif s == "-": flag = 2
        elif flag == 1:
            answer += int(s)
            flag = 0
        elif flag == 2:
            answer -= int(s)
            flag = 0
    return answer