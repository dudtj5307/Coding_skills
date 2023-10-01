a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    score_a, score_b, score_c = 0, 0, 0
    for i, num in enumerate(answers):
        if num == a[i%5]: score_a += 1
        if num == b[i%8]: score_b += 1
        if num == c[i%10]: score_c += 1
    answer = []
    if score_a == max([score_a, score_b, score_c]): answer.append(1)
    if score_b == max([score_a, score_b, score_c]): answer.append(2)
    if score_c == max([score_a, score_b, score_c]): answer.append(3)
    return answer