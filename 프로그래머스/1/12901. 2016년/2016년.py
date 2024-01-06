days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
name = ['FRI','SAT','SUN','MON','TUE','WED','THU']

def solution(a, b):
    return name[(sum(days[:a-1]) + b-1) % 7]