def solution(m, n, puddles):
    graph = [[1 for x in range(m)] for y in range(n)]
    for px, py in puddles:
        if px == 1:
            for y in range(py-1, n):
                graph[y][0] = 0
        if py == 1:
            for x in range(px-1, m):
                graph[0][x] = 0
        graph[py-1][px-1] = 0
        
    for x in range(1, m):
        for y in range(1, n):
            if graph[y][x]:
                graph[y][x] = graph[y-1][x] + graph[y][x-1]
    return graph[n-1][m-1] % 1000000007
                