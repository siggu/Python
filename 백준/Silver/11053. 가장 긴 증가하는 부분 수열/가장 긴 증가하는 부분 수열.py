N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        # print(f'i = {i}, j = {j}')
        if A[i] > A[j] and dp[i] < dp[j]:
            # print(f'A[i] = {A[i]}, A[j] = {A[j]}')
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))