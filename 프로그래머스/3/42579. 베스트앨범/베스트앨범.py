def solution(genres, plays):
    _dict = {x:[] for x in genres}
    for i in range(len(genres)):
        _dict[genres[i]].append([plays[i],i])
    
    genres_list = []
    for i,j in _dict.items():
        _list = sorted(j, key=lambda x: -x[0])
        genres_list.append([_list[:2],sum([x for x,_ in _list])])

    genres_list_sort = sorted(genres_list, key= lambda x: -x[1])
    # 장르전체재생량 기준으로 sort
    answer = []
    for i, v in genres_list_sort:
        for k,l in sorted(i,key = lambda x: (-x[0], x[1])):
        # 재생량 기준으로 sort
            answer.append(l)
    return answer