import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    x, y = map(int, input().split())

    arr.append((x, y))

arr.sort()

for x in arr:
    print(x[0], x[1])