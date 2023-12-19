def solution(n):
    r_sThree = ""
    while n > 0:
        n, r = divmod(n, 3)
        r_sThree += str(r)
    return int(r_sThree, 3)
