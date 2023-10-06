d = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}

def solution(numbers):
    q, answer = "", ""
    for n in numbers:
        q += n
        if q in d.keys():
            answer += d[q]
            q = ""
    return int(answer)