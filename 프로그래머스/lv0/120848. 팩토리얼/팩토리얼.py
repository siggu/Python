def solution(n):
    dp = []
    cnt = 0
    
    for i in range(1, 12):
        result = 1
        for j in range(1, i):
            result *= j
        dp.append(result)
    
    for k in range(1, 11):
        if dp[k] > n:
            return k-1
        elif dp[k] >= n:
            return k