import sys
read = sys.stdin.readline

N, K = map(int, read().rstrip().split())
arr = [True] * (N+1)
cnt = 0

for i in range(2, N+1):
    for j in range(i, N+1, i):
        if arr[j]:
            arr[j] = False
            cnt += 1

        if cnt == K:
            print(j)
            exit()