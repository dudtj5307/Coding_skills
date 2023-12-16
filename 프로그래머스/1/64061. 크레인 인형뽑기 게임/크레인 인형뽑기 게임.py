def solution(board, moves):
    q = []
    answer = 0
    for m in moves:
        for i in range(len(board)):
            target = board[i][m-1]
            if target != 0:
                board[i][m-1] = 0
                break
        if target == 0:
            continue
        q.append(target)
        if len(q) >= 2 and q[-1] == q[-2]:
            q = q[:-2]
            answer += 2
    return answer