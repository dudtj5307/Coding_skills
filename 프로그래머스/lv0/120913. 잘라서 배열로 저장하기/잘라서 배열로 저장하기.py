def solution(my_str, n):
    answer = []
    for i in range(len(my_str)//n):
        answer.append(my_str[n*i:n*(i+1)])
    if my_str[n*(i+1):]:
        answer.append(my_str[n*(i+1):])
    return answer