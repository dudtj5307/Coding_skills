from collections import defaultdict

def solution(msg):
    dic = defaultdict(int)
    for i in range(0, 26):
        dic[chr(ord('A')+i)] = i + 1
    next_idx = 27
    answer = []
    i = 0
    while i < len(msg):
        for j in range(i+1, len(msg)+1):
            string = msg[i:j]
            if dic[string]:
                temp = dic[string]
            else:
                answer.append(temp)
                dic[string] = next_idx
                next_idx += 1
                break
        else:
            i += 1
            answer.append(temp)  
        i += len(string) - 1
    return answer