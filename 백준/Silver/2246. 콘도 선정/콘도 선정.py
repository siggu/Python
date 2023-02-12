import sys
input = sys.stdin.readline

n = int(input())
condo = []
max_num = 10001

for _ in range(n):
    condo.append(list(map(int, input().rstrip().split())))

condo.sort()
cnt = 0

for i in condo:
    value = i[1]

    if value < max_num:
        max_num = value
        cnt += 1

print(cnt)