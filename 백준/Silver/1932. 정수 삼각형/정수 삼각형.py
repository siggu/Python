"""
        7               [7]
      3   8             [10(7+3), 15(7+8)]
    8   1   0           [18(7+3+8), 16(7+8+1), 15(7+8+0)]
  2   7   4   4         [20(7+3+8+2), 25(7+3+8+7), 20(7+8+1+4), 19(7+8+0+4)]
4   5   2   6   5       [24(7+3+8+2+4), 30(7+3+8+7+5), 27(7+3+8+7+2), 26(7+8+1+4+6), 24(7+8+0+4+5)]
"""
import sys
read = sys.stdin.readline

n = int(read())
dp = []

for _ in range(n):
    dp.append(list(map(int, read().rstrip().split())))

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif i == j:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(max(max(dp)))