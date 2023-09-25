def solution(board):
    
    def win(p):
        r,c,d = 0,0,0
        for row in range(3):
            if board[row] == p*3: r += 1
        for col in range(3):
            if [board[i][col] for i in range(3)] == [p,p,p]: c+=1
        if r > 1 or c > 1: return "NS"
        if [board[0][0], board[1][1], board[2][2]] == [p, p, p]: d+=1
        if [board[0][2], board[1][1], board[2][0]] == [p, p, p]: d+=1
        return r+c+d

    n_O, n_X = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] =="O": n_O += 1
            elif board[i][j] =="X": n_X += 1
    
    if n_O > 5 or n_O - n_X > 1 or n_O < n_X: return 0

    w_O, w_X = win("O"), win("X")
    if w_O == "NS" or w_X == "NS": return 0
    if w_O > 0 and w_X > 0: return 0

    if n_O == n_X and w_O >= 1: return 0
    if n_O > n_X and w_X >= 1: return 0
    
    return 1