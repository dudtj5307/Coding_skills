def solution(sequence):
    sequence = [val * (-1 if i % 2 else 1) for i, val in enumerate(sequence)]
    for i in range(0, len(sequence)-1): sequence[i+1] += sequence[i]
    return max(max(sequence)-min(sequence), abs(max(sequence)), abs(min(sequence)))