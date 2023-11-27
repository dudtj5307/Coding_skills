from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    n = len(begin)
    dic = {w:0 for w in words}
    dic[begin] = 1
    q = deque([begin])
    while q:
        start = q.popleft()
        for word in words:
            diff = 0
            for i in range(n):
                if start[i] != word[i]:
                    diff += 1
            if diff == 1 and not dic[word]:
                dic[word] = dic[start] + 1
                q.append(word)
    return dic[target] - 1
    
    