T = int(input())
a = list(map(int, input().split()))
dp = [0] * 80001
ans = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        ans += i
    dp[i] = ans

for i in a:
    print(dp[i])