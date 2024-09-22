def solution(sticker):
    if len(sticker) <= 2: return max(sticker)
    dp0 = [0 for _ in range(len(sticker)-1)]
    dp1 = [0 for _ in range(len(sticker))]
    # First Sticker Selected
    dp0[0], dp0[1] = sticker[0], sticker[0]
    for i in range(2, len(dp0)):
        dp0[i] = max(dp0[i-2] + sticker[i], dp0[i-1])
    # First Sticker Unselected
    dp1[0], dp1[1] = 0, sticker[1]
    for i in range(2, len(dp1)):
        dp1[i] = max(dp1[i-2] + sticker[i], dp1[i-1])
    return max(dp0[-1], dp1[-1])