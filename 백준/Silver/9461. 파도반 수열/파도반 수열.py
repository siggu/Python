'''
P(1) : 1
P(2) : 1
P(3) : 1
P(4) : 2
P(5) : 2
P(6) : 3
P(7) : 4
P(8) : 5
P(9) : 7
P(10) : 9
P(11) : 12
P(12) : 16

P(8) = P(6) + P(5) -> P(N) = P(N-2) + P(N-3)
P(8) = P(6) + P(4) -> P(N) = P(N-2) + P(N-4)

P(N) = P(N-2) + P(N-3) 적용
P(12) = P(10) + P(9)
16 = 9 + 7
'''
import sys
read = sys.stdin.readline

N = int(read())
dp = [0, 1, 1, 1] + [0] * 97

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(N):
    num = int(read())
    print(dp[num])