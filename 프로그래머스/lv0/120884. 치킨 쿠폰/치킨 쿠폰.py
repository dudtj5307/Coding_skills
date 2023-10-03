def solution(chicken):
    answer = 0
    while chicken >= 10:
        mok, nam = chicken // 10, chicken % 10
        answer += mok
        chicken = mok + nam
    return answer