from collections import defaultdict

def record(string):
    d_str = defaultdict(int)
    for i in range(len(string)-1):
        if string[i:i+2].isalpha():
            d_str[string[i:i+2].lower()] += 1
    return d_str

def solution(str1, str2):
    d_str1, d_str2 = record(str1), record(str2)
    if d_str1 == {} and d_str2 == {}: return 65536
    d_intersect, d_union = defaultdict(int), defaultdict(int)
    for key in (set(d_str1.keys()) | set(d_str2.keys())):
        d_intersect[key] = min(d_str1[key], d_str2[key])
        d_union[key]     = max(d_str1[key], d_str2[key])
    return int(65536 * sum(d_intersect.values()) / sum(d_union.values()))
    