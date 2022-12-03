import sys
read = sys.stdin.readline

n = int(read())
dp = [[False] * n for i in range(n)]
num = list(map(int, read().rstrip().split()))

for i in range(n):
    for start in range(n):
        end = start + i
        
        if end >= n:
            break
            
        if i == 0:
            dp[start][end] = True
            continue
        
        if i == 1:
            if num[start] == num[end]:
                dp[start][end] = True
                continue
        
        if num[start] == num[end] and dp[start + 1][end - 1]:
            dp[start][end] = True

m = int(read())

for i in range(m):
    a, b = map(int, read().rstrip().split())
    if dp[a - 1][b - 1]:
        print(1)
    else:
        print(0)