def solution(my_string, s, e):
    return my_string[:s]+my_string[e-len(my_string):s-len(my_string)-1:-1] + my_string[e+1:]