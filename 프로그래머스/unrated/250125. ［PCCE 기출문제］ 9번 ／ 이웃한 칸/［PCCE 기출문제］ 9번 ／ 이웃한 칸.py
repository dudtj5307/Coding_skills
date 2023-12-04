def solution(board, h, w):
    n = len(board)
    answer = []
    for dh, dw in [(-1,0), (1,0), (0,-1), (0,1)]:
        if 0 <= h +dh < n and 0 <= w + dw < n:
            answer.append(board[h +dh][w + dw])
    return answer.count(board[h][w])