def solution(word):
    w_dict = {"A":0, "E":1, "I":2, "O":3, "U":4}
    rank = 0
    for i, w in enumerate(word):
        for j in range(0, 5-i):
            rank += 5 ** j * w_dict[w]
        rank += 1
    return rank