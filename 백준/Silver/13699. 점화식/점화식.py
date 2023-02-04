"""
t(1) = t(0) * t(0) = 1
t(2) = t(0)*t(1) + t(1)*t(0) = 2
t(3) = t(0)*t(2) + t(1)*t(1) + t(2)*t(0) = 5
t(4) = t(0)*t(3) + t(1)*t(2) + t(2)*t(1) + t(3)*t(0)
t(n) = t(0)*t(n-1) + t(1)*t(n-2) + ... t(n-1)*t(0)
"""
n = int(input())
dp = [1, 1, 2, 5] + [0] * 32

for i in range(4, 36):

    for j in range(i):

        dp[i] += dp[j]*dp[i-j-1]

print(dp[n])