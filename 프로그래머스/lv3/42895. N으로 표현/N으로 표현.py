def solution(N, number):
    dp = []
    for i in range(1, 9):
        case = set()
        case.add(int(str(N) * i))
        for j in range(0, i-1):
            for num1 in dp[j]:
                for num2 in dp[-1-j]:
                    case.add(num1 + num2)
                    case.add(num1 - num2)
                    case.add(num1 * num2)
                    if num2:
                        case.add(num1 // num2)
        dp.append(case)
        if number in case: return i
    return -1