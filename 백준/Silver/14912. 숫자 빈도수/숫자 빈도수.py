import sys
read = sys.stdin.readline

n, d = map(int, read().rstrip().split())
cnt = 0

for i in range(1, n+1):
    i = str(i)
    for j in i:
        if str(d) == j:
                cnt += 1

print(cnt)