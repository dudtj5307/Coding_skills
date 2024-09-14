m = [(0,1), (1,0), (0,-1), (-1,0)]

def solution(rows, columns, queries):
    matrix = [[j+1 for j in range(columns*i, columns*(i+1))] for i in range(rows)]
    answer = []
    for idx, (si, sj, ei, ej) in enumerate(queries):
        si, sj, ei, ej = si-1, sj-1, ei-1, ej-1     # Sequence to Index
        ci, cj = si, sj
        way = 0
        next_num = matrix[si][sj]
        temp = [next_num]
        while True:
            if not (si <= ci+m[way][0] <= ei and sj <= cj+m[way][1] <= ej):
                way += 1
                if way == 4: break
            next_i, next_j = ci+m[way][0], cj+m[way][1]
            matrix[next_i][next_j], next_num = next_num, matrix[next_i][next_j]
            ci, cj = next_i, next_j
            temp.append(next_num)
        answer.append(min(temp))
    return answer