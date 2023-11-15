def solution(arr, k):
    return [k * a for a in arr] if k % 2 else [k + a for a in arr]