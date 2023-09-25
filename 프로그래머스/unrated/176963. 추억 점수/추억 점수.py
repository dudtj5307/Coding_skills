def solution(name, yearning, photo):
    y_dict = {name[i]:yearning[i] for i, n in enumerate(name)}
    result = []
    for ph in photo:
        score = 0
        for p in ph:
            if p in list(y_dict.keys()): score += y_dict[p]
        result += [score]
    return result
            