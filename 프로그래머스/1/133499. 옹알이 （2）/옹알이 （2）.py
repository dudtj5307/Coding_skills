def solution(babbling):
    d = {"aya": "0", "ye": "1", "woo": "2", "ma": "3"}
    answer = 0
    for bab in babbling:
        bab1, bab2 = "", ""
        for b in bab:
            bab1, bab2 = bab1 + b, bab2 + b
        for w in d.keys():
            bab1 = bab1.replace(w, ' ')
            bab2 = bab2.replace(w, d[w])
        if bab1.strip() == "":
            add = 1
            for s in ['00', '11', '22', '33']:
                if s in bab2:
                    add = 0
            answer += add
    return answer