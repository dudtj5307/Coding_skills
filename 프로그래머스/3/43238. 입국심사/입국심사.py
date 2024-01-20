def solution(n, times):
    left, right = 1, n * max(times)
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for t in times:
            people += mid // t
            if people >= n: break
        if people >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer

            