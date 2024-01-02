def solution(ingredient):
    ingredient = "".join(map(str, ingredient))
    answer = 0
    stack = ""
    for i in ingredient:
        stack += i
        while len(stack) >= 4 and stack[-4:] == "1231":
            stack = stack[:-4]
            answer += 1
    return answer