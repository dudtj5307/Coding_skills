def solution(picture, k):
    answer = []
    for pic in picture:
        temp = ""
        for p in pic:
            temp += p * k
        for _ in range(k):
            answer.append(temp) 
    return answer