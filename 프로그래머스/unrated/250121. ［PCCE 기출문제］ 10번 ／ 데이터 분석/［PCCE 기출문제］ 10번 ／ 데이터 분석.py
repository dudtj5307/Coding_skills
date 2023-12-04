def solution(data, ext, val_ext, sort_by):
    d = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    return sorted(list(filter(lambda x: x[d[ext]] <= val_ext, data)), key=lambda x: x[d[sort_by]])