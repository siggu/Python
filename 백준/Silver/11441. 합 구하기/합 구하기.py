import sys
read = sys.stdin.readline

N = int(read())
arr = list(map(int, read().rstrip().split()))
sum_arr = [arr[0]]

for i in range(1, N):
    sum_arr.append(sum_arr[-1] + arr[i])

M = int(read())

for _ in range(M):
    i, j = map(int, read().rstrip().split())

    if i == 1:
        print(sum_arr[j-1])
    else:
        print(sum_arr[j-1] - sum_arr[i-2])