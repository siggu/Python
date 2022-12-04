import sys
read = sys.stdin.readline

n, k = map(int, read().rstrip().split())
medal = []

for i in range(n):
    medal.append(list(map(int, read().rstrip().split())))

medal.sort(key=lambda x : (-x[1], -x[2], -x[3]))

for i in range(n):
    if medal[i][0] == k:
        index = i

for i in range(n):
    if medal[index][1:] == medal[i][1:]:
        print(i+1)
        break