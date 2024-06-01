def check_2x2(b):
    m, n = len(b), len(b[0])
    to_delete = set()
    for i in range(m-1):
        for j in range(n-1):
            if b[i][j] != "0" and b[i][j] == b[i+1][j] == b[i][j+1] == b[i+1][j+1]:
                to_delete.update([(i,j), (i+1,j), (i,j+1), (i+1,j+1)])
    return to_delete
    
def delete_2x2(b, to_delete):
    m, n = len(b), len(b[0])
    for i, j in to_delete:
        b[i][j] = "0"
    b_90 = list(map("".join, zip(*b[::-1])))        # 90도 회전
    b_90 = [b.replace("0", "") for b in b_90]       # 0 인 블럭 빼주기
    b_90 = [b + "0"*(m-len(b)) for b in b_90]       # 뒤로 0 채워주기
    b = list(map(list, zip(*b_90)))[::-1]       # -90도 회전 원복
    return b
    
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        to_del = check_2x2(board)
        if len(to_del) == 0: break
        answer += len(to_del)
        board = delete_2x2(board, to_del)
    return answer
        