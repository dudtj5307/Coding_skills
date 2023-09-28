def solution(n, costs):
    costs = sorted(costs, key=lambda x: (x[2], x[0], x[1]))
    parent = [i for i in range(n)]
    answer = 0
    for c1, c2, c3 in costs:
        if parent[c1] != parent[c2]:
            tmp_c2 = parent[c2]
            for i in range(n):
                if parent[i] == tmp_c2: 
                    parent[i] = parent[c1]                
            answer += c3
    return answer
            