def solution(chicken):
    answer, c = 0, 0
    while chicken >= 10:
        mok, nam = chicken // 10, chicken % 10
        answer += mok
        chicken = mok + nam
    return answer