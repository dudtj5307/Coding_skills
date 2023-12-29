def solution(string):
    l, temp = [], []
    temps = ""
    for s in string[1:-1]:
        if s == "{": 
            temp = []
        elif s == ",":
            temp.append(int(temps))
            temps = ""
        elif s == "}":
            if temps: temp.append(int(temps))
            l.append(temp)
        elif s.isnumeric(): 
            temps += s

    answer = []
    for array in sorted(l, key=lambda x: len(x)):
        for a in array:
            if a not in answer:
                answer.append(a)
    return answer