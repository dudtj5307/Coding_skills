def solution(dartResult):
    scores, temp = [], ""
    for d in dartResult:
        if d.isnumeric() and temp and not temp[-1].isnumeric(): 
            scores.append(temp)
            temp = d
        else: temp += d
    scores.append(temp)
    
    d = {'S':1, "D":2, "T":3}
    answer = []
    for i in range(len(scores)):
        score = scores[i]
        num = ""
        while score[0].isnumeric():
            num += score[0]
            score = score[1:]
        answer.append(int(num) ** d[score[0]])
        if len(score) >= 2:
            if score[1] == "*":
                answer[i] *= 2
                if i >= 1: answer[i-1] *= 2
            else:
                answer[i] *= -1
    return sum(answer)
                
        