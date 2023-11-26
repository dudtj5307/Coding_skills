def solution(arr):
    n = (len(arr) + 1)//2
    MAX_DP = [[-float('inf') for _ in range(n)] for _ in range(n)]
    MIN_DP = [[float('inf') for _ in range(n)] for _ in range(n)]
    ops = {i: arr[i*2 + 1] for i in range(n-1)}
    for i in range(n):
        a = int(arr[i*2])
        MAX_DP[i][i], MIN_DP[i][i] = a, a
    
    for step in range(1, n):
        for i in range(n-step):
            j = i + step
            for k in range(i,j):
                if arr[k*2 + 1] == '+':
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k+1][j])
                else:
                    MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k+1][j])
                    MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k+1][j])
    return MAX_DP[0][n-1]