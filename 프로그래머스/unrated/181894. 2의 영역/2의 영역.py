def solution(arr):
    idx_list = []
    if 2 not in arr: return [-1]
    for i in range(len(arr)):
        if arr[i] == 2:
            idx_list.append(i)
    return arr[min(idx_list):max(idx_list)+1]