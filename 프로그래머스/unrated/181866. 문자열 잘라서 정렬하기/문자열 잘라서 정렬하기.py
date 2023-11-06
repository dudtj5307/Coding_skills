def solution(myString):
    answer = []
    for m in myString.split('x'):
        if m != "":
            answer.append(m)
    return sorted(answer)