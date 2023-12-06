def solution(board, k):
    m, n = len(board), len(board[0])
    answer = 0
    for i in range(m):
        for j in range(n):
            if i + j <= k:
                answer += board[i][j]
    return answer