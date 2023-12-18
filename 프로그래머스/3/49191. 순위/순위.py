def solution(n, results):
    table = [[0 for _ in range(n)] for _ in range(n)]
    for winner, loser in results:
        table[winner-1][loser-1] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if table[i][j] == 0 and table[i][k] and table[k][j]:
                    table[i][j] = 1
    answer = 0
    for i in range(n):
        if sum(table[i]) + sum(list(map(lambda x: x[i], table))) == n-1:
            answer += 1
    return answer