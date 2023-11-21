def solution(arr):
    col, row = len(arr), len(arr[0])
    if col > row:
        for i in range(col):
            arr[i].extend([0]*(col-row))
    elif col < row:
        for _ in range(row - col):
            arr.append([0]*row)
            
    return arr