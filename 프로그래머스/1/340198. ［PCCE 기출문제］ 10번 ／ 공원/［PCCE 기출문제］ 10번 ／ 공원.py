def solution(mats, park):
    N, M = len(park), len(park[0])
    
    def search(si, sj):
        max_search_size = min(N-si, M-sj)
        for n in range(1, max_search_size):
            for i in range(n+1):
                if park[si+i][sj+n] != "-1" or park[si+n][sj+i] != "-1":
                    return n
        return max_search_size
    
    max_size = 0
    for i in range(N):
        for j in range(M):
            if park[i][j] == "-1":
                max_size = max(max_size, search(i,j))
    answer = list(filter(lambda x:x<=max_size, mats))
    if len(answer) == 0: return -1
    else: return max(answer)