def solution(target):
    dp = [[float('inf'), 0] for _ in range(target+1)]
    dp[0] = [0,0]
    for i in range(0, target):
        count, single = dp[i]
        if target >= i + 50:    # Bull
            if dp[i+50][0] > count + 1:
                dp[i+50] = [count + 1, single + 1]
            elif dp[i+50][0] == count + 1:
                dp[i+50][1] = max(dp[i+50][1], single + 1)
                
        for j in range(1, 21):
            if target >= i + j:     # Single
                if dp[i+j][0] > count + 1:
                    dp[i+j] = [count + 1, single + 1]
                elif dp[i+j][0] == count + 1:
                    dp[i+j][1] = max(dp[i+j][1], single + 1)
            if target >= i + 2*j and dp[i+2*j][0] > count + 1:   # Double
                dp[i+2*j] = [count + 1, single]
            if target >= i + 3*j and dp[i+3*j][0] > count + 1:   # Triple
                dp[i+3*j] = [count + 1, single]
    return dp[-1]
            
                
                