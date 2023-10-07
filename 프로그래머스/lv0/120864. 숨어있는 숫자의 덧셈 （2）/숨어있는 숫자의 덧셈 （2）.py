def solution(my_string):
    answer = 0
    num = ""
    for s in my_string:
        if s.isnumeric():
            num += s
        elif num:
            answer += int(num)
            num = ""
    if num: answer += int(num)
    return answer
                