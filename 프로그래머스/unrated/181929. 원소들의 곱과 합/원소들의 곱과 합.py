def solution(num_list):
    a, b = 1, 0
    for n in num_list:
        a *= n
        b += n
    return 1 if a < b**2 else 0