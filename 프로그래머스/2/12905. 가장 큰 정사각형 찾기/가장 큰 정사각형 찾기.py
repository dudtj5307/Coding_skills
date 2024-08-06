def solution(board):
    m, n = len(board), len(board[0])
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    return max(map(lambda b: max(b), board)) ** 2