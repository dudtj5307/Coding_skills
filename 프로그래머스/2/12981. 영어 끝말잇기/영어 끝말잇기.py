from collections import defaultdict

def solution(n, words):
    dic = defaultdict(int)
    last = words[0][0]
    for i in range(len(words)):
        word = words[i]
        if last != word[0] or dic[word]:
            return [i % n +1, i // n + 1]
        else:
            dic[word] = 1
            last = word[-1]
    return [0,0]