from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 102 for _ in range(102)]
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[y][x] = 0
                elif graph[y][x] != 0:
                    graph[y][x] = 1
    characterX, characterY = characterX * 2, characterY * 2
    graph[characterY][characterX] = 0
    q = deque([[characterX, characterY]])
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 102 and 0 <= ny < 102 and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                q.append([nx, ny])
            if nx == itemX*2 and ny == itemY*2:
                return graph[ny][nx] // 2