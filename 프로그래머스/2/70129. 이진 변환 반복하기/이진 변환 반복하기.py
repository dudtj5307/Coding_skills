def solution(s):
    i, cnt = 0, 0
    while s != "1":
        cnt1 = s.count("1")
        cnt += len(s) - cnt1
        s = bin(cnt1)[2:]
        i += 1
    return [i, cnt]