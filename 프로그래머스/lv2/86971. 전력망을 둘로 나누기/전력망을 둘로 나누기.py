from collections import Counter

def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        wire = wires[:i] + wires[i+1:]
        parent = [p for p in range(1, n+1)]
        for w in wire:
            a, b = sorted(w)
            temp = parent[b-1]
            parent[b-1] = parent[a-1]
            for i in range(n):
                if parent[i] == temp: parent[i] = parent[a-1]
        c1, c2 = Counter(parent).values()
        answer = min(answer, abs(c1-c2))
    return answer
        
        