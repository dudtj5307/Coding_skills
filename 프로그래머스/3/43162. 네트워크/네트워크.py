def solution(n, computers):
    link = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                if link[i] <= link[j]:
                    front, back = link[i], link[j]
                else:
                    front, back = link[j], link[i]
                for k in range(n):
                    if link[k] == back:
                        link[k] = front
                if link[i] <= link[j]:
                    link[j] = link[i]
                else:
                    link[i] = link[j]
    return len(set(link))