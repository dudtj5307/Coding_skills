dict_key = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right": (1,0)}

def solution(keyinput, board):
    sx, sy, bx, by = 0, 0, board[0]//2, board[1]//2
    for k in keyinput:
        k = dict_key[k]
        if -bx <= sx + k[0] <= bx and -by <= sy + k[1] <= by:
            sx += k[0]
            sy += k[1]
    return [sx, sy]