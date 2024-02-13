from collections import defaultdict

def solution(edges):
    node = defaultdict(lambda: [0,0]) # [나간수, 들어오는수]
    for s, e in edges:
        node[s][0] += 1
        node[e][1] += 1
    answer = [0, 0, 0, 0]
    for n, counts in node.items():
        out, inn = counts
        if out >= 2 and inn == 0:
            answer[0] = n
        elif out == 0 and inn >= 1:
            answer[2] += 1
        elif out >= 2 and inn >= 2:
            answer[3] += 1
    answer[1] = node[answer[0]][0] - answer[2] - answer[3]
    return answer
    