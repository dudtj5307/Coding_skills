d = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2], 0:[3,1]}

def solution(numbers, hand):
    left, right = [3,0], [3,2]
    answer = ""
    for n in numbers:
        if n in {1,4,7}:
            answer += "L"
            left = d[n]
        elif n in {3,6,9}:
            answer += "R"
            right = d[n]
        else:
            i, j = d[n]
            dleft = abs(left[0]-i) + abs(left[1]-j)
            dright = abs(right[0]-i) + abs(right[1]-j)
            if dleft > dright:
                answer += "R"
                right = d[n]
            elif dleft < dright:
                answer += "L"
                left = d[n]
            else:
                if hand == "left":
                    answer += "L"
                    left = d[n]
                else:
                    answer += "R"
                    right = d[n]                 
    return answer