def solution(my_string, queries):
    n = len(my_string)
    for s, e in queries:
        my_string = my_string[:s] + my_string[e-n:s-n-1:-1] + my_string[e+1:]
    return my_string